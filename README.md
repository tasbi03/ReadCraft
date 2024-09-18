
# 🎉 Welcome to the README Generator (ReadCraft) 🎉

This handy tool automatically crafts a new `README.md` file from your code! 💻✨ All you have to do is point the tool to your code file, and boom – you get a beautifully crafted README using the Groq API. 🚀

## 📽 Demo

Here’s a quick demo of the tool in action:

![README Generator Demo](./assets/demo_simple.gif)

---

## 💡 Features

- 🛠 **README Generation**: Just give it some code, and it will generate a professional README for you.
- 🗂 **Multiple Files? No Problem**: Generate READMEs for more than one file at a time!
- 🔐 **Flexible API Key Setup**: Use either a `.env` file or pass your API key directly through the command line.
- 📂 **Custom Output**: Save your new README in any directory you like.
- 🧠 **Choose Your AI Model**: You can either specify a custom model from Groq or let the script use its default one.

---

## 🛠 Prerequisites

Make sure you have the following installed:
- **Python 3.7+**🐍
- `pip` (Python package manager) to install the required packages.

---

## 🚀 How to Set Up

### 1. Clone the Repo

First things first – grab a copy of this project on your local machine:

```sh
git clone https://github.com/your-username/readme_generator.git
cd readme_generator
```

### 2. Install Dependencies

Next, install the necessary Python packages:

```sh
pip install -r requirements.txt
```

This will set you up with all the required libraries like `requests`, `python-dotenv`, and others.

---

## 🔑 Setting Up Your API Key

You can provide your Groq API key in two ways:

### Option 1: Use a `.env` File

1. Create a `.env` file in the project root (or rename `sample.env` to `.env`).
2. Add your Groq API key to the `.env` file like this:

```env
GROQ_API_KEY=YOUR_API_KEY
```

3. Then run the script without having to pass the key on the command line:

```sh
python readme_generator.py path/to/your/input/file.py
```

This will run the script with the **default AI model** specified in the code.

### Option 2: Pass API Key via Command Line

Don’t want to mess with `.env` files? No problem! Just pass the key like this:

```sh
python readme_generator.py path/to/your/input/file.py --api-key YOUR_API_KEY
```

This will also run the script with the default AI model.

---

## 🧠 Specifying a Custom AI Model

If you want to use a specific AI model, simply provide it with the `--model` argument.

```sh
python readme_generator.py path/to/your/input/file.py --model your_custom_model
```

You can also combine this with your API key:

```sh
python readme_generator.py path/to/your/input/file.py --api-key YOUR_API_KEY --model your_custom_model
```

If no model is provided, the script will fall back to using the **default model** defined in the code.

---

## 🗂 Custom Output Directory

By default, the generated `README.md` will be saved in the `./output` folder. But if you want to change that, just specify the folder like this:

```sh
python readme_generator.py path/to/your/input/file.py --output-dir ./your_output_dir --model your_model_name
```

---

## 📜 Running the Script

Here’s an example of running the script with the default model:

```sh
python readme_generator.py example.py
```

Or, specifying both an API key and a custom model:

```sh
python readme_generator.py example.py --api-key YOUR_API_KEY --model your_custom_model
```

---

## 🔍 Finding Your Generated README

🎉 Your freshly generated `README.md` file will be waiting for you in the folder you specified!

- If you didn't specify an output directory, the default is `./output`.
- If you used an output directory, check there! For example:

```sh
python readme_generator.py example.py --output-dir ./crafted_readme --model mixtral-8x7b-32768
```

Your file will be in `crafted_readme`.

---

## 💡 Example Commands

```sh
# Using the .env file and default model:
python readme_generator.py example.py

# Specify a custom output directory and default model:
python readme_generator.py example.py --output-dir ./crafted_readme

# Passing API key and specifying a custom model:
python readme_generator.py example.py --api-key YOUR_API_KEY --model your_custom_model
```

---

## Examples

To test the tool, you can use the provided examples in the `examples/` directory.

### Example usage:
```sh
python readme_generator.py examples/sample.py --api-key YOUR_API_KEY --model mixtral-8x7b-32768
```
---

## 🛠 Troubleshooting

- **No API key provided?** Check that your `.env` file is correct or pass the API key via command line.
- **File not found?** Make sure the path to your input file is correct.
- **Output directory issues?** Don’t worry – the directory will be created automatically if it doesn’t exist.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 📞 Need Help?

Have questions or issues? Open an issue in the repository, and we’ll be happy to help you out!
