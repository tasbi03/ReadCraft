from pathlib import Path
import argparse
import requests
from dotenv import load_dotenv
import os
import sys  # Required for output control (stdout, stderr)
import json  # For JSON output

# Load environment variables from a .env file (if available)
load_dotenv()

def generate_readme(file_contents, api_key, model, stream=False):
    """
    Generates a README for the provided code file using the Groq API.
    If stream is True, stream the results as they arrive.

    Args:
        file_contents (str): The content of the code file.
        api_key (str): The API key required for authorization with the Groq API.
        model (str): The AI model to use for generating the README.
        stream (bool): Whether to stream the response in real-time.

    Returns:
        str: The generated README content, or None if the request fails.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    # Prepare the API request payload
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a README file for the following code:\n{file_contents}"}
        ],
        "max_tokens": 1000  # Limit the number of tokens for the response
    }

    # Set the headers with the authorization token
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # If streaming is enabled, use stream=True in the request
        response = requests.post(url, json=payload, headers=headers, timeout=10, stream=stream)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        if stream:
            # Stream the response content line by line
            for chunk in response.iter_lines():
                if chunk:
                    # Decode each chunk
                    chunk_data = json.loads(chunk.decode('utf-8'))
                    
                    # Extract and print only the assistant's message content
                    if "choices" in chunk_data:
                        content = chunk_data["choices"][0]["message"]["content"]
                        print(content, flush=True)  # Print the content as it streams
            return None  # Return None since we're streaming directly to stdout
        else:
            # Standard response handling for non-streaming mode
            return response.json().get('choices')[0]['message']['content']

    except requests.exceptions.Timeout:
        print("Error: The request timed out.", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    
# get the token usage for the api and output it to the console
def getTokenUsage(api_key, model):
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Prepare the payload for the API request
    payload = {
        "model": model,  # Now using the model passed from the command line
        "messages": [
            {"role": "user", "content": f"Get token usage info"}
        ],
        "max_tokens": 1000
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        # Add a timeout of 10 seconds to prevent hanging
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error if the response code is 4xx or 5xx
        return response.json().get('usage')
    except requests.exceptions.Timeout:
        print("Error: The request timed out.", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # Initialize the argument parser for handling CLI inputs
    parser = argparse.ArgumentParser(description="CLI tool for generating README files using the Groq API.")

    # Optional flag to print the tool's version
    parser.add_argument('--version', '-v', action='version', version='ReadCraft README Generator Tool 1.0')

    # Required positional argument for one or more input files to process
    parser.add_argument('files', nargs='*', help="Specify one or more input files to generate README for")

    # Optional flag for specifying the API key (falls back to .env if not provided)
    parser.add_argument('--api-key', '-a', type=str, help="Specify the API key for Groq API (optional, will use .env if not provided)")

    # Optional flag to specify the output directory for saving the generated README files
    parser.add_argument('--output-dir', '-o', type=str, help="Specify the output directory for the generated README files")

    # Optional flag for selecting the AI model (default is 'mixtral-8x7b-32768')
    parser.add_argument('--model', '-m', type=str, default='mixtral-8x7b-32768', help="Specify the AI model to use")

    # Optional flag to print the token usage
    parser.add_argument('--token-usage', '-t',action='store_true', help="Get token usage of the API")

     # Add the --json flag for JSON output
    parser.add_argument('--json', action='store_true', help='Output results in JSON format')

    # Add the --stream flag for streaming output
    parser.add_argument('--stream', '-s', action='store_true', help='Stream responses in real-time')


    # Parse command-line arguments
    args = parser.parse_args()

    # Obtain the API key either from command-line or .env file
    api_key = args.api_key or os.getenv("GROQ_API_KEY")

    # Check for token usage
    if args.token_usage:
        print(getTokenUsage(api_key, args.model))

    # Proceed with README generation even if token usage is requested
    # If no API key is provided, log an error and exit the script
    if not api_key:
        print("Error: No API key provided. Use --api-key or set GROQ_API_KEY in .env", file=sys.stderr)
        sys.exit(1)

    # If an output directory is specified, create it if it doesn't exist
    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)

    # List to store results for JSON output
    results = []
    all_success = True  # Track overall success for exit codes

    # Iterate over each input file specified
    for file in args.files:
        file_path = Path(file)

        # Validate if the file exists
        if not file_path.exists():
            print(f"Error: {file_path} does not exist.", file=sys.stderr)
            all_success = False
            continue

        # Open and read the file contents
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"Processing file: {file}", file=sys.stderr)

            # Stream or standard processing logic
            if args.stream:
                accumulated_content = []
                for chunk in response.iter_lines():
                    if chunk:
                        chunk_data = json.loads(chunk.decode('utf-8'))
                        if "choices" in chunk_data:
                            content = chunk_data["choices"][0]["message"]["content"]
                            accumulated_content.append(content)
                            if not args.json:  # Print in real-time if not using JSON
                                print(content, flush=True)
                # If JSON flag is enabled, append to results for final output
                if args.json:
                    result = {"file": file, "readme_content": accumulated_content, "status": "success"}
                    results.append(result)
            else:
                # Generate the README using the API in non-streaming mode
                readme_content = generate_readme(content, api_key, args.model)
                result = {
                    "file": file,
                    "readme_content": readme_content,
                    "status": "success" if readme_content else "failure"
                }

                # Output the result based on the flags
                if readme_content:
                    if args.output_dir:
                        output_file = output_dir / f"{file_path.stem}_README.md"
                        with open(output_file, 'w') as readme_file:
                            readme_file.write(readme_content)
                        if args.json:
                            json_output_file = output_dir / f"{file_path.stem}_README.json"
                            with open(json_output_file, 'w') as json_file:
                                json.dump(result, json_file, indent=2)
                        print(f"README generated and saved as {output_file}")
                    else:
                        print(readme_content, file=sys.stdout)
                else:
                    print(f"Error: Failed to generate README for {file_path}", file=sys.stderr)
                    all_success = False
                results.append(result)

    # Print the accumulated JSON output if --json is used and no output directory is provided
    if args.json and not args.output_dir:
        print(json.dumps(results, indent=2))

    # Exit with success (0) or failure (1)
    sys.exit(0 if all_success else 1)
