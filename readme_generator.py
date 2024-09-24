from pathlib import Path
import argparse
import requests
from dotenv import load_dotenv
import os
import sys  # Required for output control (stdout, stderr)
import json  # For JSON output

# Load environment variables from a .env file (if available)
load_dotenv()

def generate_readme(file_contents, api_key, model):
    """
    Generates a README for the provided code file using the Groq API.

    Args:
        file_contents (str): The content of the code file.
        api_key (str): The API key required for authorization with the Groq API.
        model (str): The AI model to use for generating the README (default model is mixtral-8x7b-32768).

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
        # Make a POST request to the Groq API with a timeout of 10 seconds
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Return the generated content from the API response
        return response.json().get('choices')[0]['message']['content']
    
    except requests.exceptions.Timeout:
        # Handle timeout exception and log to stderr
        print("Error: The request timed out.", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        # Handle any other request-related exceptions and log to stderr
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
    parser.add_argument('--token-usage', '-t', action='store_true', help="Get token usage of the API")

    # Add the --json flag for JSON output
    parser.add_argument('--json', action='store_true', help='Output results in JSON format')

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

    # Iterate over each input file or directory specified
    for file in args.files:
        file_path = Path(file)

        # Check if input is a directory
        if file_path.is_dir():
            # Warn if directory is empty
            if not any(file_path.iterdir()):
                print(f"Warning: Directory {file_path} is empty.", file=sys.stderr)

            # Recursively process all files in the directory
            for subfile in file_path.rglob('*'):
                if subfile.is_file():
                    # Process each file as normal
                    print(f"Processing file: {subfile}", file=sys.stderr)
                    with open(subfile, 'r') as f:
                        content = f.read()
                        readme_content = generate_readme(content, api_key, args.model)

                        result = {
                            "file": str(subfile),
                            "readme_content": readme_content,
                            "status": "success" if readme_content else "failure"
                        }

                        # Save results based on flags
                        if readme_content:
                            if args.output_dir:
                                output_file = output_dir / f"{subfile.stem}_README.md"
                                json_output_file = output_dir / f"{subfile.stem}_README.json"
                                
                                with open(output_file, 'w') as readme_file:
                                    readme_file.write(readme_content)
                                
                                if args.json:
                                    with open(json_output_file, 'w') as json_file:
                                        json.dump(result, json_file, indent=2)
                                
                                print(f"README generated and saved as {output_file}")
                                if args.json:
                                    print(f"JSON output saved as {json_output_file}")
                            else:
                                print(readme_content, file=sys.stdout)
                        else:
                            print(f"Error: Failed to generate README for {subfile}", file=sys.stderr)
                            all_success = False

                        # Add result to JSON list
                        results.append(result)

        # Process individual files
        elif file_path.is_file():
            print(f"Processing file: {file_path}", file=sys.stderr)

            with open(file_path, 'r') as f:
                content = f.read()
                readme_content = generate_readme(content, api_key, args.model)

                result = {
                    "file": str(file_path),
                    "readme_content": readme_content,
                    "status": "success" if readme_content else "failure"
                }

                # Save results based on flags
                if readme_content:
                    if args.output_dir:
                        output_file = output_dir / f"{file_path.stem}_README.md"
                        json_output_file = output_dir / f"{file_path.stem}_README.json"
                        
                        with open(output_file, 'w') as readme_file:
                            readme_file.write(readme_content)
                        
                        if args.json:
                            with open(json_output_file, 'w') as json_file:
                                json.dump(result, json_file, indent=2)
                        
                        print(f"README generated and saved as {output_file}")
                        if args.json:
                            print(f"JSON output saved as {json_output_file}")
                    else:
                        print(readme_content, file=sys.stdout)
                else:
                    print(f"Error: Failed to generate README for {file_path}", file=sys.stderr)
                    all_success = False

                # Add result to JSON list
                results.append(result)

        else:
            error_message = f"Error: {file_path} does not exist."
            print(error_message, file=sys.stderr)
            results.append({"file": str(file_path), "error": error_message})
            all_success = False

    # Print JSON output if --json is used and no output directory is provided
    if args.json and not args.output_dir:
        print(json.dumps(results, indent=2))

    # Exit with success (0) or failure (1) based on overall results
    sys.exit(0 if all_success else 1)
