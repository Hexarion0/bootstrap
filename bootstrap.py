from pathlib import Path
import os
import subprocess
import datetime


# -------------------------
# Utilities
# -------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_file(path, content=""):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


# -------------------------
# Source File
# -------------------------

def create_source_file(name, language, location=""):

    extensions = {
        "Python": "py",
        "JavaScript": "js",
        "Java": "java",
        "C#": "cs",
        "C++": "cpp",
        "C": "c",
        "TypeScript": "ts",
        "Go": "go",
        "Rust": "rs"
    }

    extension = extensions[language]


    if location:
        source = Path(name) / location / f"{name}.{extension}"
    else:
        source = Path(name) / f"{name}.{extension}"


    templates = {

        "py": 'print("Hello World!")\n',

        "js": 'console.log("Hello World!");\n',

        "java": """public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
""",

        "cs": """using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello World!");
    }
}
""",

        "cpp": """#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
""",

        "c": """#include <stdio.h>

int main() {
    printf("Hello World!");
    return 0;
}
""",

        "ts": 'console.log("Hello World");\n',

        "go": """package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
""",

        "rs": """fn main() {
    println!("Hello World!");
}
"""
    }


    write_file(
        source,
        templates[extension]
    )


# -------------------------
# README
# -------------------------

def create_readme(name, language, license_name):

    content = f"""# {name}

Generated with Hexarion Bootstrap 🚀


## Language

{language}


## License

{license_name}


## Created

{datetime.date.today()}


## Usage

TODO: Add instructions here
"""


    write_file(
        Path(name) / "README.md",
        content
    )


# -------------------------
# Gitignore
# -------------------------

def create_gitignore(name, language):

    ignores = {

        "Python":
"""__pycache__/
*.pyc
.env
venv/
dist/
build/
""",

        "JavaScript":
"""node_modules/
.env
dist/
build/
""",

        "TypeScript":
"""node_modules/
.env
dist/
build/
""",

        "Java":
"""*.class
target/
.idea/
""",

        "C#":
"""bin/
obj/
.vscode/
""",

        "C++":
"""*.o
*.out
build/
""",

        "C":
"""*.o
*.out
build/
""",

        "Go":
"""bin/
*.exe
""",

        "Rust":
"""target/
Cargo.lock
"""
    }


    write_file(
        Path(name) / ".gitignore",
        ignores.get(language, "")
    )


# -------------------------
# License
# -------------------------

def create_license(name, license_type):

    licenses = {

        "MIT":
f"""MIT License

Copyright (c) {datetime.date.today().year} {name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software.
""",

        "Apache 2.0":
"""Apache License 2.0

Licensed under the Apache License, Version 2.0.
""",

        "BSD 3-Clause":
"""BSD 3-Clause License

Redistribution and use in source and binary forms are permitted.
""",

        "GPL v3":
"""GNU GENERAL PUBLIC LICENSE Version 3

This program is free software.
"""
    }


    if license_type in licenses:

        write_file(
            Path(name) / "LICENSE",
            licenses[license_type]
        )


# -------------------------
# Git
# -------------------------

def git_init(name):

    try:

        subprocess.run(
            ["git", "init", name],
            check=True
        )

    except Exception:

        print("Git initialization failed")


# -------------------------
# Main
# -------------------------

def main():

    clear()


    print("""
╔════════════════════════════╗
║  Hexarion Bootstrap v1.0   ║
╚════════════════════════════╝
""")


    name = input("Project name: ")


    languages = [
        "Python",
        "JavaScript",
        "Java",
        "C#",
        "C++",
        "C",
        "TypeScript",
        "Go",
        "Rust"
    ]


    print("\nLanguages:")

    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")


    choice = int(
        input("\nChoose language: ")
    )


    if choice < 1 or choice > len(languages):

        print("Invalid language")
        return


    language = languages[choice-1]


    # License

    licenses = [
        "MIT",
        "Apache 2.0",
        "BSD 3-Clause",
        "GPL v3",
        "None"
    ]


    print("\nLicenses:")

    for i, lic in enumerate(licenses, 1):
        print(f"{i}. {lic}")


    license_choice = int(
        input("\nChoose license: ")
    )


    if license_choice < 1 or license_choice > len(licenses):

        print("Invalid license")
        return


    license_name = licenses[license_choice-1]


    # Create folder

    create_directory(name)


    # Optional folders

    src_choice = input("\nCreate src folder? (y/n): ")

    tests_choice = input("Create tests folder? (y/n): ")


    location = ""


    if src_choice.lower() == "y":

        create_directory(
            f"{name}/src"
        )

        location = "src"


    if tests_choice.lower() == "y":

        create_directory(
            f"{name}/tests"
        )


    # Files

    create_source_file(
        name,
        language,
        location
    )


    create_readme(
        name,
        language,
        license_name
    )


    create_gitignore(
        name,
        language
    )


    if license_name != "None":

        create_license(
            name,
            license_name
        )


    # Git

    git = input(
        "\nInitialize git repository? (y/n): "
    )


    if git.lower() == "y":

        git_init(name)


    clear()


    print(f"""
✅ Project Created!

Name: {name}
Language: {language}
License: {license_name}


Created:

{name}/
├── README.md
├── .gitignore
├── LICENSE
├── src/ (optional)
├── tests/ (optional)
└── source file


Happy coding 🚀
""")


if __name__ == "__main__":
    main()