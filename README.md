
# 🎉 Welcome to ReadCraft - The README Generator 🎉

**ReadCraft** helps you automatically create professional `README.md` files for your code using the Groq API. 🚀

Simply point it to your code, and let the tool generate a well-structured README for you in no time! 💻✨

## 📽 Quick Demo

![README Generator Demo](./assets/demo_simple.gif)

---

## 💡 Key Features

- 🗂 **Process Multiple Files or Directories**: Generate READMEs for individual files or entire directories.
- 🌊 **Real-Time Streaming**: Watch your README being generated in real-time, streamed directly to your terminal.
- 🛠 **Easy README Generation**: Feed in your code, and receive a professional README file.
- 🔐 **Flexible API Key Setup**: Use a `.env` file or pass your API key directly via command line.
- 📂 **Custom Output Directory**: Choose where to save your generated `README.md` files.
- 🧠 **Choose Your AI Model**: Use the default model or specify a custom one.

---

## 🛠 Prerequisites

Ensure the following are installed:
- **Python 3.7+** 🐍
- `pip` (for package management)

---

## 🚀 Setup Instructions

### Step 1: Clone the Repository

Start by cloning the repository to your local machine:

```sh
git clone https://github.com/your-username/readme_generator.git
cd readme_generator
```

### Step 2: Install Dependencies

Run the following command to install all the required packages:

```sh
pip install -r requirements.txt
```

### Step 3: Manual Installation of `python-dotenv`

To handle `.env` files, the tool uses `python-dotenv`. If it isn't installed, use:

```sh
pip install python-dotenv
```

---

## 🔑 Setting Up Your API Key

You can provide your Groq API key in two ways:

### Option 1: Use a `.env` File

1. Create a `.env` file in the project root (or rename `sample.env` to `.env`).
2. Add your API key:

```env
GROQ_API_KEY=YOUR_API_KEY
```

3. Run the script:

```sh
python readme_generator.py path/to/your/input/file.py
```

### Option 2: Pass the API Key via Command Line

You can also pass your API key directly:

```sh
python readme_generator.py path/to/your/input/file.py --api-key YOUR_API_KEY
```

---

## 🧠 Specify a Custom AI Model

If you'd like to use a specific AI model, provide the `--model` argument:

```sh
python readme_generator.py path/to/your/input/file.py --model your_custom_model
```

---

## 🗂 Processing Entire Directories

Easily generate READMEs for all files in a directory:

```sh
python readme_generator.py /path/to/your/code_directory --api-key YOUR_API_KEY
```

---

## 🌊 Stream the Output in Real-Time

Want to see the README while it's being generated? Use the `--stream` flag:

```sh
python readme_generator.py path/to/your/input/file.py --stream
```

---
## 📄 JSON Output

Want to save the output as a JSON file in addition to the `README.md`? Just use the `--json` flag:

```sh
python readme_generator.py path/to/your/input/file.py --json

# This will create both a README.md and a JSON file containing the generated content. You can combine this with other flags, such as specifying an output directory or streaming:
python readme_generator.py path/to/your/input/file.py --json --output-dir ./your_output_dir

#If you want to combine it with real-time streaming:
python readme_generator.py path/to/your/input/file.py --json --stream

#This will stream the output to your terminal while also saving the results to both .md and .json files.
```

---

## 📂 Customize the Output Directory

By default, READMEs are saved in `./output`. To change the location:

```sh
python readme_generator.py path/to/your/input/file.py --output-dir ./your_output_dir
```

---

## 📜 Running the Script

Examples:

```sh
# Default model and .env API key:
python readme_generator.py example.py

# Custom output directory and model:
python readme_generator.py example.py --output-dir ./crafted_readme --model your_model_name

# Process an entire directory:
python readme_generator.py /path/to/your/code_directory --output-dir ./crafted_readmes

# Full example with custom model, API key, streaming, and JSON output:
python readme_generator.py ./my_files --model mixtral-8x7b-32768 --api-key your-api-key --json --output-dir ./test_output_multiple --stream
```

---
## Configuration via TOML File

This tool now supports specifying default configuration values using a TOML-formatted configuration file in the user's home directory. This allows you to avoid passing the `--api-key` and `--model` arguments every time you run the tool.

### How to Set Up the Configuration File

1. **Create the TOML file in your home directory**:
   Create a file named `.your-toolname-config.toml` in your home directory (`~`).

2. **Add your API key and model to the file**:
   In this file, you can define default values for the `api_key` and `model`. For example:
   ```toml
   api_key = "your_api_key_here"
   model = "your_model_here"
   ```
3. **Usage**:
- If the TOML config file is present, the tool will automatically load these values when run.
- If you provide --api-key or --model as command-line arguments, they will override the values from the TOML file.

4. **File Location**:
- The file should be placed in the home directory (~), and the filename should be .your-toolname-config.toml (a dotfile).

### Example
```toml
# Running the tool with the configuration from the TOML file
python readme_generator.py path_to_your_input_file_or_directory

# Overriding the TOML file values with command-line arguments
python readme_generator.py path_to_your_input_file_or_directory --api-key "override_api_key" --model "override_model"
```
By using this configuration file, you can avoid repeatedly entering sensitive data like API keys on the command line, while still allowing flexibility to override values as needed.

## Running with Token Usage

You can also track token usage with the `--token-usage` flag:

```sh
python readme_generator.py file1.py --api-key Your_API_Key --token-usage
```

---

## 🔍 Finding Your Generated README

- If no output directory is specified, your README will be in the default `./output` folder.
- If you provided an output directory, check there for the file!

Example:

```sh
python readme_generator.py example.py --output-dir ./crafted_readme
```

---

## 🛠 Troubleshooting

- **No API Key?** Make sure your `.env` file is correctly configured or pass the API key via the command line.
- **File Not Found?** Double-check the path to your input file or directory.
- **Output Directory Issues?** The directory will be automatically created if it doesn’t exist.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

## 📞 Need Help?

Have questions? Open an issue in the repository, and we’ll be happy to assist!
