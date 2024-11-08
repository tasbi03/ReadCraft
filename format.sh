#!/bin/bash
# Run Black only on core project files and directories
black . 

# Run Flake8 for linting
flake8 .