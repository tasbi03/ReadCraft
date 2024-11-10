
# 🛠 Troubleshooting Guide

This guide provides solutions to common issues while working on *ReadCraft*. Use these steps to troubleshoot effectively.

---

## 1. Running Tests

#### Running All Tests
Run all tests with:
```bash
pytest
```

#### Import Errors in Tests
If you see a `ModuleNotFoundError`, try setting the Python path:
```bash
PYTHONPATH=. pytest
```

#### Running a Specific Test File or Test Function
- **Single Test File**:
  ```bash
  pytest tests/test_generate_readme.py
  ```
- **Single Test Function**:
  ```bash
  pytest tests/test_generate_readme.py::test_generate_readme_success
  ```

#### Verbose Output for Debugging
To see which tests passed or failed with details:
```bash
PYTHONPATH=. pytest -v
```

---

## 2. Code Formatting and Linting

#### Automatic Formatting with Black
Run Black to format:
```bash
black .
```

#### Checking for Linting Issues with Flake8
Run Flake8 to catch code style issues:
```bash
flake8 .
```

#### Fixing VSCode Formatting/Linting Issues
If Black or Flake8 doesn’t auto-run:
1. Open VSCode settings (Preferences > Settings).
2. Set “Python formatting provider” to `black`.
3. Ensure `"editor.formatOnSave": true` is enabled.

---

## 3. Dependency Issues

#### Ensure `pip` is Up-to-Date
Update `pip` with:
```bash
python -m pip install --upgrade pip
```

#### Reinstall Dependencies
If there are errors with dependencies:
```bash
pip install -r requirements.txt
```

#### Manually Installing Missing Packages
If specific packages aren’t found, try:
```bash
pip install pytest pytest-watch flake8 black python-dotenv toml
```

---

## 4. Code Coverage Troubleshooting

#### Coverage Command Not Found
If `coverage` isn’t installed, run:
```bash
pip install coverage
```

#### Coverage Report Shows Unexpected Missing Lines
This can happen if code is conditionally executed or indirectly referenced. Try checking for:
- Error handling blocks
- Conditional paths (e.g., `if` statements with untested branches)
- Lines where exceptions may occur

#### HTML Report Not Opening
After running `coverage html`, open the file directly:
```bash
open htmlcov/index.html
```

If that doesn’t work, manually navigate to the `htmlcov` folder and open `index.html`.

---

## 5. Debugging Failing Tests

#### Running with Verbosity
Run with `-v` for more details:
```bash
PYTHONPATH=. pytest -v
```

#### Debugging a Specific Test
Run only the failing test file or function:
```bash
PYTHONPATH=. pytest tests/test_generate_readme.py::test_generate_readme_success
```

#### Using Python Debugger (pdb)
Add `import pdb; pdb.set_trace()` in the code for interactive debugging.

---

## 6. Additional Notes for Mocks

Ensure mocks are correctly defined, especially for API calls. Any external API keys or tokens should be mocked or set in `.env`.

---

We hope this guide helps resolve any issues! If you're still stuck, feel free to reach out by creating an issue, for more assistance.
