
# README Generator

This project is a command-line tool that generates a `README.md` file for your project by sending the code to the Groq API, which uses an AI model to automatically create a detailed README based on the source files.

## Features
- Command-line interface (CLI) to input source code files
- Uses Groq's AI API to analyze code and generate a well-structured `README.md`
- Supports multiple input files
- Automatically saves generated README files to an output directory
- Allows API key input via command line or `.env` file

## Prerequisites
To use this tool, you need to have the following installed:

- Python 3.7+
- An API key from Groq (can be added manually or via `.env` file)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tasbi03/Release-1.git
   cd Release-1
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root of the project:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

You can use this tool by running the following command:

```bash
python readme_generator.py --api-key YOUR_API_KEY file1.py file2.py ...
```

### Optional Arguments:
- `--api-key`, `-a`: Passes the API key directly. If not provided, the tool will attempt to load the API key from the `.env` file.
- `--output-dir`, `-o`: Specifies the directory where the generated README files will be saved (default is `./output`).

### Example:

```bash
python readme_generator.py -a YOUR_API_KEY main.py utils.py -o ./docs
```

This will generate README files for `main.py` and `utils.py` and save them in the `docs` directory.

## .gitignore
Make sure to exclude your `.env` and virtual environment (`venv`) from version control by adding the following to `.gitignore`:

```
# Ignore virtual environment
venv/

# Ignore environment variables
.env
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
