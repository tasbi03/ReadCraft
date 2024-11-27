
# 🎉 Welcome to Contributing to ReadCraft!

Thank you for considering joining the *ReadCraft* community! We’re excited to have you on board. This guide will walk you through setting up your environment and give you a quick tour of our code standards, testing practices, and troubleshooting tips. Let’s make contributing easy, efficient, and enjoyable! 🌟

---

## 🛠 Development Setup

### Prerequisites

You’ll need:
- *Python 3.7+* 🐍
- *pip* (for managing packages)

### Getting Started with the Project

1. *Clone the Repository*:
   ```sh
   git clone https://github.com/your-username/readme_generator.git
   cd readme_generator
   ```
2. *Set Up a Virtual Environment (recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
2. *Install Dependencies*:
   ```sh
   pip install -r requirements.txt
   ```

3. *Install Additional Packages* (for .env and TOML support):
   ```sh
   pip install python-dotenv toml
   ```

All set! 🎉

---

## 🔧 Code Formatting and Linting

We use *Black* for formatting and *Flake8* for linting to keep code clean and consistent.

### Formatting and Linting in VSCode

1. Open the project in *VSCode* or *GitHub Codespaces*.
2. Install recommended extensions:
   - Python
   - Black Formatter
   - Flake8 Linter

3. Black auto-formats on save, and Flake8 catches issues in real-time. ✨

### Manual Formatting and Linting

Run Black and Flake8 manually if needed:
```sh
black .
flake8 .
```

---

## 🧪 Running Tests

Testing is essential for a reliable project! We use `pytest` and `unittest.mock` for mocking API responses.

### Running All Tests

To run all tests, use:
```sh
pytest
```

### Running a Specific Test or Test File

- **Single Test File**:
  ```sh
  pytest tests/test_generate_readme.py
  ```
- **Single Test Function**:
  ```sh
  pytest tests/test_generate_readme.py::test_generate_readme_success
  ```

### Troubleshooting Test Runs

Sometimes, `pytest` might not recognize imports. If you see `ModuleNotFoundError`, try running:
```bash
PYTHONPATH=. pytest
```

For more details, check out our [TROUBLESHOOTING.md](TROUBLESHOOTING.md) file!

---

## 🛠 Git Pre-Commit Hook: Automate Formatting & Linting

Add a pre-commit hook to run Black and Flake8 automatically on files being committed.

### Setting Up the Pre-Commit Hook

1. *Create the Hook File*:
   In `.git/hooks/pre-commit`, add:
   ```bash
   #!/bin/bash
   black .
   flake8 .
   ```

2. *Make It Executable*:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

---

## 📈 Code Coverage Analysis

To ensure comprehensive testing, we use code coverage analysis to check which parts of the codebase are tested. This helps identify any untested paths.

### Running Code Coverage

1. **Install Coverage** (if not already installed):
   ```bash
   pip install coverage
   ```

2. **Run Coverage with Tests**:
   ```bash
   coverage run -m pytest
   ```

3. **View Coverage Report**:
   - **Terminal Report**: Display coverage results directly in the terminal.
     ```bash
     coverage report
     ```
   - **HTML Report**: Generate a detailed HTML report to explore coverage visually.
     ```bash
     coverage html
     ```
   Open `htmlcov/index.html` in your browser to see coverage details.

4. **Improving Coverage**:
   - Review uncovered lines in the report.
   - Add missing tests to cover edge cases or error handling paths.

---

Thank you for helping make *ReadCraft* awesome! Your contributions make a difference, and we’re thrilled to have you with us. Let’s build something amazing together! 🚀
