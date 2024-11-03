#!/bin/bash
# Run Black only on core project files and directories
black readme_generator.py 

# Run Flake8 for linting
flake8 .