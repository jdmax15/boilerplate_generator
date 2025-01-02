import sys
from pathlib import Path

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main module for the boilerplate generator project.
"""

def create_project(project_name):
    current_dir = Path.cwd()
    project_dir = current_dir / project_name
    project_dir.mkdir(exist_ok=True)

    main_file = project_dir / "main.py"
    functions_file = project_dir / "functions.py"

    main_file.touch()
    functions_file.touch()

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