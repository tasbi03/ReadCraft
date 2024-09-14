from pathlib import Path
import argparse
import requests
from dotenv import load_dotenv
import os
import sys  # Import sys for stdout and stderr

# Load the API key from the .env file
load_dotenv()

def generate_readme(file_contents, api_key, model):
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Prepare the payload for the API request
    payload = {
        "model": model,  # Now using the model passed from the command line
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a README file for the following code:\n{file_contents}"}
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
        return response.json().get('choices')[0]['message']['content']
    except requests.exceptions.Timeout:
        print("Error: The request timed out.", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="README Generator CLI Tool")

    # Add arguments for version and help
    parser.add_argument('--version', '-v', action='version', version='README Generator 1.0')

    # Add the required argument for input files
    parser.add_argument('files', nargs='+', help="One or more input files")

    # Add argument for specifying the API key
    parser.add_argument('--api-key', '-a', type=str, help="API key for Groq (optional, will use .env if not provided)")

    # Add argument for output directory
    parser.add_argument('--output-dir', '-o', type=str, default='./output', help="Output directory for the generated README files")

    # Add argument for model selection (configurable)
    parser.add_argument('--model', '-m', type=str, default='mixtral-8x7b-32768', help="Specify the AI model to use")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Use the API key from the command line or fallback to the one in .env
    api_key = args.api_key or os.getenv("GROQ_API_KEY")

    if not api_key:
        print("Error: No API key provided. Use --api-key or set GROQ_API_KEY in .env", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)

    # Ensure the output directory exists
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    # Process each file
    for file in args.files:
        file_path = Path(file)

        if not file_path.exists():
            print(f"Error: {file_path} does not exist.", file=sys.stderr)
            continue  # Skip to the next file

        with open(file_path, 'r') as f:
            content = f.read()
            print(f"Processing file: {file}", file=sys.stderr)

            # Generate README
            readme_content = generate_readme(content, api_key, args.model)
            if readme_content:
                # Save the README content to the specified directory
                output_file = output_dir / f"{file_path.stem}_README.md"
                with open(output_file, 'w') as readme_file:
                    readme_file.write(readme_content)
                print(f"README generated and saved as {output_file}", file=sys.stderr)
            else:
                print(f"Error: Failed to generate README for {file_path}", file=sys.stderr)
