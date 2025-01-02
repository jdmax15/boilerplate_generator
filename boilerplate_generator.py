import sys
from pathlib import Path

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main module for the boilerplate generator project.
Navigate to the directory where you want to create a new project and run the script (C:\SCRIPTS\boilerplate_generator.bat + *directory name*) with the project name as the CLI input.

The script will create a new directory with the project name and create the following files:
- main.py (with boilerplate code)
- functions.py
- README.md

"""

def create_project(project_name):
    current_dir = Path.cwd()
    project_dir = current_dir / project_name
    project_dir.mkdir(exist_ok=True)

    main_file = project_dir / "main.py"
    functions_file = project_dir / "functions.py"
    readme_file = project_dir / "README.md"

    main_file.touch()
    functions_file.touch()
    readme_file.touch()

    boilerplate_code = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
Main module for the project.
\"\"\"

import sys
from functions import *

def main():
    \"\"\"
    Main entry point for the script.
    \"\"\"
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""

    with main_file.open("w") as f:
        f.write(boilerplate_code)

    print(f"Project '{project_name}' created successfully at {project_dir}")

def main():
    """
    Main entry point for the script.
    """
    if len(sys.argv) != 2:
        sys.exit("Please enter a project/directory name as the CLI input.")
    else:
        project_name = sys.argv[1]
        create_project(project_name)

if __name__ == "__main__":
    main()