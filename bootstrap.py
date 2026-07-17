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
# Dependency Files
# -------------------------

def create_dependency_file(name, language, location=""):

    base_path = Path(name)
    if location:
        base_path = base_path / location

    dependencies = {

        "Python": """# Dependencies for {name}
# Add your packages here, e.g.:
# requests>=2.25.1
# numpy>=1.20.0
""",

        "JavaScript": """{
  "name": "{name}",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
""",

        "TypeScript": """{
  "name": "{name}",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "typescript": "^4.0.0"
  }
}
""",

        "Java": """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>{name}</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <!-- Add your dependencies here -->
    </dependencies>
</project>
""",

        "C#": """<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>OutputType>
    <TargetFramework>net6.0)</TargetFramework>
    >Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <!-- Add your packages here -->
  </ItemGroup>

</Project>
""",

        "C++": """# CMakeLists.txt for {name}
cmake_minimum_required(VERSION 3.10)
project({name})

set(CMAKE_CXX_STANDARD 17)

add_executable({name} main.cpp)

# Add your libraries here
# target_link_libraries({name} PRIVATE some_library)
""",

        "C": """# CMakeLists.txt for {name}
cmake_minimum_required(VERSION 3.10)
project({name})

set(CMAKE_C_STANDARD 11)

add_executable({name} main.c)

# Add your libraries here
# target_link_libraries({name} PRIVATE some_library)
""",

        "Go": """module github.com/yourusername/{name}

go 1.16

// Add your dependencies here
// example.com/some/module v1.2.3
""",

        "Rust": """[package]
name = "{name}"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
# Add your dependencies here
# rand = "0.8"
"""
    }

    # Determine file name based on language
    filenames = {
        "Python": "requirements.txt",
        "JavaScript": "package.json",
        "TypeScript": "package.json",
        "Java": "pom.xml",
        "C#": f"{name}.csproj",
        "C++": "CMakeLists.txt",
        "C": "CMakeLists.txt",
        "Go": "go.mod",
        "Rust": "Cargo.toml"
    }

    filename = filenames.get(language)
    if not filename:
        return

    template = dependencies.get(language, "")
    if not template:
        return

    content = template.format(name=name)
    file_path = base_path / filename
    write_file(file_path, content)


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
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""",

        "Apache 2.0":
"""Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

Copyright {year} {author}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.""",

        "BSD 2-Clause":
"""BSD 2-Clause License

Copyright (c) {year} {author}

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.""",

        "BSD 3-Clause":
"""BSD 3-Clause License

Copyright (c) {year}, {author}
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.""",

        "GPL v3":
"""GNU GENERAL PUBLIC LICENSE
   Version 3, 29 June 2007

 Copyright (C) {year} {author}

 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.""",

        "LGPL v3":
"""GNU LESSER GENERAL PUBLIC LICENSE
   Version 3, 29 June 2007

 Copyright (C) {year} {author}

 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.""",

        "MPL 2.0":
"""Mozilla Public License Version 2.0

==========================================================================

  1. Definitions.

  1.1. "Contributor"
       means each individual or legal entity that creates, contributes to
       the creation of, or owns software that is included in a Contributor Version.

  1.2. "Contributor Version"
       means the combination of the Contributions of others (if any) used
       by a Contributor and that particular Contributor's Contribution.

  1.3. "Contribution"
       means Covered Software of a particular Contributor.

  1.4. "Covered Software"
       means Source Code Form to which the initial Contributor is attached,
       and the Executable Form of such Source Code Form.

  1.5. "Incompatible With Secondary Licenses"
       means

       * that the initial Covered Software is not in Secondary Licensed Material;
       * that the initial Covered Software is Incompatible With Secondary Licenses
         if the initial Covered Software is not a Secondary License;
       * that the initial Covered Software is a Secondary License but the initial
         Contributor has not attached an Exhibit B to its contribution;
         or
       * that the initial Covered Software is a Secondary License but the initial
         Contributor has attached a subsequent version of an Exhibit B to its
         contribution that has not been approved by the Steward.

  1.6. "Executable Form"
       means any form of the work other than Source Code Form.

  1.7. "Larger Work"
       means a work that combines Covered Software with material that is not
       Covered Software. If a Larger Work is a combination of Covered Software
       with one or more unrelated pieces of software or data, the Larger Work
       may not be distributed with respect to Covered Software under this License
       unless

       * the Larger Work is a combination of Covered Software with one or more
         separate files whose licenses are compatible with this License, and
       * the Larger Work is a combination of Covered Software with one or more
         separate files whose licenses are incompatible with this License, and

         the Larger Work is provided to the respective recipients of each of
         those files with a notice in conspicuous form (printed in connection
         with the distribution of the Covered Software or provided as a separate
         document) stating that the Larger Work combines Covered Software with
         material that is not Covered Software, and that the requirements of
         this License with respect to the Larger Work are satisfied.

  1.8. "Secondary License"
       means either the GNU General Public License, Version 2.0,
       the GNU Lesser General Public License, Version 2.1,
       or the GNU Affero General Public License, Version 3.0.

  1.9. "Source Code Form"
       means the form of the work preferred for making modifications.

  1.10. "Standards Track"
        means a specification that is under consideration for, has been adopted
        by, or is in the process of being adopted by a standards organization.

  1.11. "Subject to Conditions"
        means that the recipient of a Covered Software must meet certain
        conditions to receive the associated Benefit.

  1.12. "Secondary Licenses"
        means the GNU General Public License, Version 2.0,
        the GNU Lesser General Public License, Version 2.1,
        or the GNU Affero General Public License, Version 3.0.

                                                                   Exhibit B - Compatibility with Secondary Licenses

  This Source Code Form is "Incompatible With Secondary Licenses", as
  defined by the Mozilla Public License, v. 2.0.""",

        "ISC":
"""ISC License

Copyright (c) {year} {author}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.""",

        "CC0":
"""Creative Commons Zero v1.0 Universal

CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
ATTORNEY-CLIENT RELATIONSHIP. PROVIDED THAT YOU AGREE TO THE FOLLOWING
TERMS AND CONDITIONS, YOU MAY COPY, DISTRIBUTE, MODIFY, AND PERFORM
THIS WORK, EVEN FOR PUBLIC PERFORMANCE, WITHOUT ANY RESTRICTION ON HOW
YOU MAY USE THE WORK.

Unless you have opted out of a jurisdiction-specific license tag, the
jurisdiction-specific license tag for this license is CC0-1.0. The legal
code of this license is the dedication above.

Statement of Purpose

The laws of most jurisdictions throughout the world currently confer
automatic copyright protection on the following types of works: "text,"
"pictures," "moving pictures" (EE. "films"), and "computer programs."
Individuals and institutions are making electronic copies of these works
available on the Internet at an increasingly rapid rate, motivated by a
variety of purposes, be they educational, in the preservation of cultural
heritage, or for pure entertainment. The volunteers who are involved in
such efforts, however, believe strongly that there is no ethical or
philosophical justification for claiming ownership, or the right to
determine the use of, these works. Our purpose in dedicating the works
to the public domain is to enable free access to information and other
cultural resources for all persons regardless of their station in life;
and to disperse concentrated accumulations of economic value that
accompany such collections, the accumulation of which is believed to
represent a misallocation of resources.

The person who associated a work with this deed has dedicated the work to
the public domain by waiving all of his or her rights to the work worldwide
under copyright law, including all related and neighboring rights,
to the extent allowable by law.

You can copy, modify, distribute and perform the work, even for commercial
purposes, all without asking permission. See http://creativecommons.org/publicdomain/zero/1.0/.""",

        "None":
"""No license selected.
All rights reserved.
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
        "BSD 2-Clause",
        "BSD 3-Clause",
        "GPL v3",
        "LGPL v3",
        "MPL 2.0",
        "ISC",
        "CC0",
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
    
    # Create dependency file
    create_dependency_file(
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
├── [dependency file]
└── source file


Happy coding 🚀
""")


if __name__ == "__main__":
    main()