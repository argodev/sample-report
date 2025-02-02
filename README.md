# Sample Report

This is a simple example of using Python to generate a report.

## Overview

- Load in the CSV file
- Generate a report with the following properties:
  - Create a unique page per church
  - On each page list the users for that church
  - List of church users should be alphabetical

## Steps/Tutorial

1. Clone this repo (or create a one). 
   ``` bash
   git clone https://github.com/argodev/sample-report.git
   ```

1. Assuming `python` is installed, create virtual environment for this project:
   ``` bash
   cd sample-report
   python3 -m venv venv
   . venv/bin/activate
   ```

1. Install some of the dependencies
   ``` bash
   pip install --upgrade pip
   pip install jinja2
   pip install pandas
   pip install xhtml2pdf
   ```

1. Once you open the directory in VS Code, set the interpreter to the current `venv`.


## Tips

The notes in the section are *purely* optional, but listed in case they are helpful.

- You might consider using the __Rainbow CSV__ extension for VS Code. It makes viewing `*.csv` files in the editor much easier.

