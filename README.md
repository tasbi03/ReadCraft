
# 🎉 Welcome to ReadCraft - The README Generator 🎉

**ReadCraft** automates the process of creating professional README.md files based on your code using the Groq API. This tool is perfect for saving time and ensuring consistent, engaging documentation for your projects!

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

### Step 1: Clone the Repository
Clone the repository to your local machine and navigate to the directory:

```sh
git clone https://github.com/your-username/readcraft.git
cd readcraft
```

### Step 2: Install Dependencies
Install all required packages:

```sh
pip install -r requirements.txt
```

### Step 2: Install Additional Packages (for handling .env and TOML files):
   ```sh
   pip install python-dotenv toml
   ```
---

## ⚙ Configuration

ReadCraft can retrieve configuration details from various sources:

1. **Environment Variables**: Create a `.env` file and add your API key:
   ```plaintext
   GROQ_API_KEY=YOUR_API_KEY
   ```

2. **TOML Config File**: Store configuration in a TOML file named `.your-toolname-config.toml` in your home directory:
   ```toml
   api_key = "your_api_key_here"
   model = "your_model_here"
   ```

---

## 📈 Usage

Generate a README with a single command! Here are some examples of how to use ReadCraft:

### Basic Usage
Generate a README for a Python file using your default API key and model:
```sh
python readme_generator.py path/to/your/file.py
```

### CLI Options and Flags

| Flag | Description | Example |
|------|-------------|---------|
| `--api-key` | Specify the API key (overrides `.env` and TOML settings). | `--api-key YOUR_API_KEY` |
| `--output-dir` | Define an output directory for generated files. | `--output-dir ./output` |
| `--model` | Choose a specific model (default is `mixtral-8x7b-32768`). | `--model custom_model` |
| `--json` | Save output as JSON. | `--json` |
| `--stream` | Stream output as it's generated. | `--stream` |
| `--token-usage` | Display token usage information. | `--token-usage` |

### Usage Examples

1. **Generate README with Custom Output Directory**:
   ```sh
   python readme_generator.py path/to/your/file.py --output-dir ./output_readme
   ```

2. **Generate README and Output as JSON**:
   ```sh
   python readme_generator.py path/to/your/file.py --json
   ```

3. **Process an Entire Directory**:
   ```sh
   python readme_generator.py /path/to/your/directory --output-dir ./output_dir
   ```

4. **Stream Output and Show Token Usage**:
   ```sh
   python readme_generator.py path/to/your/file.py --stream --token-usage
   ```

5. **Run Complete Process with a Single Command**:
   To generate the README, stream output, save it as JSON, and show token usage in one command, use:
   ```sh
   python readme_generator.py ./my_files --output-dir ./outputdir --stream --json --token-usage

   #This way, users can perform all actions in one command without needing extra setup in the code.

   ```

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
2. **Install dependencies** listed in `requirements.txt` and dev dependencies like `Black` and `Flake8`.
3. **Run Pre-Commit Hooks**: Set up pre-commit hooks to automatically format and lint your code:
   ```sh
   chmod +x .git/hooks/pre-commit
   ```

For more details, see [CONTRIBUTING.md](contributing.md).

---

## 🛠 Troubleshooting

**Common Issues**:
- **No API Key**: Ensure your API key is set in `.env` or passed with `--api-key`.
- **Timeouts**: Increase timeout in the code if API calls frequently time out.
- **Configuration Conflicts**: Double-check that `.env` and `.your-toolname-config.toml` settings don’t contradict each other.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


