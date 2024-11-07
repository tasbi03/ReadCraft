
# 🎉 Welcome to Contributing to ReadCraft!

Thank you for considering joining the *ReadCraft* community! We’re excited to have you on board. This guide will walk you through setting up your environment and give you a quick tour of our code standards. Let's make contributing easy, efficient, and enjoyable! 🌟

---

## 🛠 Development Setup

### Prerequisites

You’ll need the following tools ready to go:
- *Python 3.7+* 🐍
- *pip* (for managing packages)

### Getting Started with the Project

1. *Clone the Repository*:
   ```sh
   git clone https://github.com/your-username/readme_generator.git
   cd readme_generator
   ```

2. *Install Dependencies*:
   ```sh
   pip install -r requirements.txt
   ```

3. *Install Additional Packages* (for handling .env and TOML files):
   ```sh
   pip install python-dotenv toml
   ```

And you’re all set up! 🎉

---

## 🔧 Code Formatting and Linting

We’ve set up *Black* for formatting and *Flake8* for linting to help keep our code clean and consistent. Your *VSCode* is configured to handle this automatically thanks to our .vscode settings, making setup a breeze!

### Setting Up in VSCode

1. *Open the Project* in *VSCode* or *GitHub Codespaces*.
2. *Install Recommended Extensions* (if prompted):
   - Python
   - Black Formatter
   - Flake8 Linter

3. *Auto-Format on Save*:
   Black will format your code every time you save a file. ✨

4. *Real-Time Linting*:
   Flake8 highlights issues as you code, keeping errors and warnings under control.

### Manual Formatting and Linting

Not using VSCode? No worries! You can run Black and Flake8 directly in the terminal:

```sh
# Run Black
black .

# Run Flake8
flake8 .
```

---

## 🧪 Running Tests

Always double-check that your code works! (If applicable, add testing instructions here to ensure every contributor can run tests smoothly.)

---

## 🛠 Git Pre-Commit Hook: Automate Formatting & Linting

Let’s make life even easier with a *Git pre-commit hook*! This hook runs Black and Flake8 automatically on any files being committed. It’s like having a safety net that catches formatting issues before they hit the repo.

### Setting Up the Pre-Commit Hook

1. *Create the Hook File*:
   In .git/hooks/pre-commit, add the following:

   ```bash
   #!/bin/bash
   black .
   flake8 .
   ```

2. *Make It Executable*:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

Now, every time you commit, this hook will check your code for formatting and linting issues, making sure your contribution meets our standards. 🎩

---

## ⚙ Configuration via TOML File

Prefer to have default settings for API keys or models? You can create a .your-toolname-config.toml file in your home directory to store these defaults:

```toml
api_key = "your_api_key_here"
model = "your_model_here"
```

This way, you won’t need to pass API keys or model options every time you run the tool.

---

Thank you for helping make *ReadCraft* awesome! Your contributions make a difference, and we’re thrilled to have you with us. Let’s build something amazing together! 🚀
