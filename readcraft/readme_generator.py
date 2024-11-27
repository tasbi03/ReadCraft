from pathlib import Path
import argparse
import requests
from dotenv import load_dotenv
import os
import sys  # Required for output control (stdout, stderr)
import json  # For JSON output
import toml  # To handle TOML config files
import logging


# Load environment variables from a .env file (if available)
load_dotenv(dotenv_path=".env")

# Setup logging configuration
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


# Utility function to handle file input/output
def handle_file_io(config_filename=".your-toolname-config.toml"):
    config_path = Path.home() / config_filename
    if config_path.exists():
        try:
            return toml.load(config_path)
        except toml.TomlDecodeError:
            logging.error(f"Failed to parse TOML config file at {config_path}")
            sys.exit(1)
    return {}


def make_api_request(api_key, model, file_contents, file_extension, stream=False):
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Determine the type of script based on the file extension
    if file_extension == ".py":
        file_type = "Python script"
    elif file_extension == ".js":
        file_type = "JavaScript script"
    else:
        file_type = "script"

    # Updated prompt with file type and instructions
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": (
                    f"Generate a README for this {file_type}:\n\n{file_contents}\n\n"
                    "Please make the README fun and engaging! Add emojis to highlight sections and "
                    "use **bold text** for important terms or section titles like 'Function', 'Usage', "
                    "and 'Examples'. Avoid unnecessary sections like 'Authors' or 'Acknowledgments'."
                ),
            },
        ],
        "max_tokens": 1000,
    }

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    try:
        if stream:
            response = requests.post(url, json=payload, headers=headers, stream=True)
            response.raise_for_status()
            accumulated_content = []
            for chunk in response.iter_lines():
                if chunk:
                    chunk_data = json.loads(chunk.decode("utf-8"))
                    if "choices" in chunk_data:
                        content = chunk_data["choices"][0]["message"]["content"]
                        logging.info(content)  # Print each streamed chunk
                        accumulated_content.append(content)
            return "\n".join(accumulated_content), {}
        else:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            content = response.json().get("choices")[0]["message"]["content"]
            token_usage = response.json().get("usage", {})
            return content, token_usage
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None, None


# Function to get token usage from the API
def get_token_usage(api_key, model):
    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Get token usage info"}],
        "max_tokens": 1000,
    }

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json().get("usage")
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None


def generate_readme(file_contents, api_key, model, file_extension, stream=False):
    # Check if file_contents is empty and handle it accordingly
    if not file_contents:
        return "No content to process"

    content, token_usage = make_api_request(
        api_key, model, file_contents, file_extension, stream
    )
    if token_usage:
        logging.info(f"Token usage: {token_usage}")
    return content


# Centralized configuration manager to handle API key, model, and output directory
class ConfigManager:
    def __init__(self, args, config):
        self.args = args
        self.config = config
        self.api_key = self.get_api_key()
        self.model = self.get_model()
        self.output_dir = self.get_output_dir()

    def get_api_key(self):
        return (
            self.args.api_key or self.config.get("api_key") or os.getenv("GROQ_API_KEY")
        )

    def get_model(self):
        return self.args.model or self.config.get("model", "mixtral-8x7b-32768")

    def get_output_dir(self):
        if self.args.output_dir:
            output_dir = Path(self.args.output_dir)
            if not output_dir.exists():
                output_dir.mkdir(parents=True, exist_ok=True)
            return output_dir
        return None


# Refactored output manager to handle saving files
class OutputManager:
    def __init__(self, output_dir, json_output):
        # Ensure output_dir is a Path object
        self.output_dir = Path(output_dir) if output_dir else None
        self.json_output = json_output

    def save_readme(self, file_path, readme_content):
        """Save the generated README content to a Markdown file."""
        if self.output_dir:
            output_file = self.output_dir / f"{file_path.stem}_README.md"
            with open(output_file, "w") as readme_file:
                readme_file.write(readme_content)
            logging.info(f"README generated and saved as {output_file}")

    def save_json(self, file_path, result):
        """Save the output result in JSON format, if required."""
        if self.output_dir and self.json_output:
            json_output_file = self.output_dir / f"{file_path.stem}_README.json"
            with open(json_output_file, "w") as json_file:
                json.dump(result, json_file, indent=2)
            logging.info(f"JSON output saved as {json_output_file}")


def main():
    # Initialize the argument parser for handling CLI inputs
    parser = argparse.ArgumentParser(
        description="CLI tool for generating README files using the Groq API."
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="ReadCraft README Generator Tool 1.0",
    )
    parser.add_argument(
        "files_or_directory",
        nargs="+",
        help="Specify one or more input files or a directory to generate README for",
    )
    parser.add_argument(
        "--api-key",
        "-a",
        type=str,
        help="Specify the API key for Groq API (optional, will use .env if not provided)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        help="Specify the output directory for the generated README files",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default="mixtral-8x7b-32768",
        help="Specify the AI model to use",
    )
    parser.add_argument(
        "--token-usage", "-t", action="store_true", help="Get token usage of the API"
    )
    parser.add_argument(
        "--json", action="store_true", help="Output results in JSON format"
    )
    parser.add_argument(
        "--stream", "-s", action="store_true", help="Stream responses in real-time"
    )

    args = parser.parse_args()
    config = handle_file_io()

    # Create a ConfigManager instance to centralize configuration handling
    config_manager = ConfigManager(args, config)

    # Create an OutputManager to handle file output
    output_manager = OutputManager(config_manager.output_dir, args.json)

    if args.token_usage:
        print(get_token_usage(config_manager.api_key, config_manager.model))

    if not config_manager.api_key:
        logging.error("No API key provided. Use --api-key or set GROQ_API_KEY in .env")
        sys.exit(1)

    results = []
    all_success = True

    for path in args.files_or_directory:
        path = Path(path)
        if path.is_dir():
            files = list(path.glob("*"))
        else:
            files = [path]

        for file_path in files:
            if not file_path.is_file():
                continue

            with open(file_path, "r") as f:
                content = f.read()
                logging.info(f"Processing file: {file_path}")

                # Pass the file extension to generate_readme
                readme_content = generate_readme(
                    content,
                    config_manager.api_key,
                    config_manager.model,
                    file_path.suffix,
                    stream=args.stream,
                )

                result = {
                    "file": str(file_path),
                    "readme_content": readme_content,
                    "status": "success" if readme_content else "failure",
                }

                if readme_content:
                    output_manager.save_readme(file_path, readme_content)
                    if args.json:
                        output_manager.save_json(file_path, result)
                else:
                    logging.error(f"Failed to generate README for {file_path}")

    if args.json and not config_manager.output_dir:
        print(json.dumps(results, indent=2))

    sys.exit(0 if all_success else 1)


# Ensures the script runs properly when executed as a command-line tool
if __name__ == "__main__":
    main()
