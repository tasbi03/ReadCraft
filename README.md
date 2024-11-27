
# 🎉 Welcome to ReadCraft - The README Generator 🎉

**ReadCraft** automates the process of creating professional `README.md` files based on your code using the Groq API. This tool is perfect for saving time and ensuring consistent, engaging documentation for your projects!

![README Generator Demo](./assets/demo_simple.gif)

## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 🌟 Overview

ReadCraft takes in your code and generates a well-structured, user-friendly README file. It also allows you to track token usage, output results in JSON format, and process directories of files at once!

## ✨ Features
- 🗂 **Multiple File Processing**: Generate READMEs for individual files or entire directories.
- 🔑 **Flexible Configuration**: Set up your API key with `.env` or pass it via command line.
- 🌊 **Real-Time Streaming**: Stream output as it’s generated with the `--stream` flag.
- 📄 **JSON Output**: Save your README as a JSON file with the `--json` option.

---

## 📥 Installation

### Prerequisites
- **Python 3.7+** 🐍
- **pip** for package management

### Installing via PyPI
Install ReadCraft directly from [PyPI](https://pypi.org/project/readcraft/):
```bash
pip install readcraft
```

---

## ⚙ Configuration

ReadCraft retrieves configuration details from various sources:

1. **Environment Variables**: Create a `.env` file and add your API key:
   ```plaintext
   GROQ_API_KEY=YOUR_API_KEY
   ```

2. **Command Line Flag**: Use the `--api-key` flag to provide the API key when running the tool:
   ```bash
   readcraft file.py --api-key YOUR_API_KEY
   ```

3. **TOML Config File**: Store configuration in a TOML file named `.your-toolname-config.toml` in your home directory:
   ```toml
   api_key = "your_api_key_here"
   model = "your_model_here"
   ```

---

## 📈 Usage

After installing `readcraft`, follow these steps to generate a `README.md` for your files.

1. **Locate the ReadCraft Installation**:
   - Run:
     ```bash
     pip show readcraft
     ```
   - Find the `Location` field in the output, which points to where ReadCraft is installed.

2. **Add the File(s)**:
   - Place the file(s) you want to generate a README for into an accessible directory or just write:
      ```bash
      cd ~
      touch file_name.py
      nano file_name.py   #In here you can copy the content of the file you want readme for and to save just press ctrl+O and exit by ctrl+X!
      readcraft file_name.py --output-dir ./outputdir  --api-key Your-API-Key --json --stream
      ```

   - Alternatively, provide the full path to the file when running the command.

3. **Run the Tool**:
   - Process a single file:
     ```bash
     readcraft /path/to/your/file.py --output-dir ./output
     ```
   - Process an entire directory:
     ```bash
     readcraft /path/to/your/directory --output-dir ./output
     ```

4. **Verify the Output**:
   - The generated `README.md` will appear in the specified output directory.

---

## 📝 Example Output

### Sample README Output
When you run the script, ReadCraft generates a README.md file based on the contents of your code:

**Example README.md**:
```markdown
# Sample Project 🚀

This project is designed to [describe key functionalities of the project here]. It’s structured to make your life easier!

## Features
- **Easy to Use**: Simple commands for quick results.
- **High Performance**: Optimized for performance with real-time streaming.
```

### Sample JSON Output
If you use the `--json` flag, an output JSON file is also created:
```json
{
  "file": "path/to/your/file.py",
  "readme_content": "# Sample Project...",
  "status": "success"
}
```

---

## 🤝 Contributing

We welcome contributions! Follow these steps to set up your environment:

1. **Fork the repository** and clone it.
2. **Install dependencies** listed in `requirements.txt`.
3. **Run Pre-Commit Hooks**: Set up pre-commit hooks to automatically format and lint your code:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

For more details, see [CONTRIBUTING.md](contributing.md).

---

## 🛠 Troubleshooting

**Common Issues**:

- **No API Key Provided**: Ensure your API key is set in a `.env` file (`GROQ_API_KEY=your_api_key`) or passed via `--api-key`.
- **Installation Errors**: Use Python 3.7+ and ensure `pip` is up to date. If issues persist, use a virtual environment.
- **Timeouts or Connection Errors**: Check your internet connection or retry after a short delay.
- **Missing Output**: Verify the input file path and ensure the `--output-dir` directory exists.
- **Configuration Conflicts**: Command-line arguments override `.env` and TOML settings. Use one method consistently.
- **Outdated Dependencies**: Upgrade critical packages (e.g., `requests`) if you encounter compatibility issues with Python 3.12+.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
