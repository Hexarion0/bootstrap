# Hexarion Bootstrap

A powerful project bootstrap tool that creates ready-to-code project structures for multiple programming languages with proper licensing, git initialization, and sensible defaults.

![GitHub](https://img.shields.io/github/license/hexarion0/bootstrap)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

## ✨ Features

- **Multi-language Support**: Generate projects for Python, JavaScript, Java, C#, C++, C, TypeScript, Go, and Rust
- **Smart Templates**: Language-appropriate "Hello World" starter files
- **License Generator**: Choose from MIT, Apache 2.0, BSD 3-Clause, or GPL v3 licenses
- **Git Integration**: Optional git repository initialization
- **Flexible Structure**: Optional `src/` and `tests/` directories
- **Proper Ignores**: Language-specific `.gitignore` files
- **Professional README**: Auto-generated project documentation
- **Interactive CLI**: User-friendly prompts for quick project setup

## 🚀 Installation

No installation required! Just clone or download the repository and run the script:

```bash
git clone https://github.com/hexarion0/bootstrap.git
cd bootstrap
python3 bootstrap.py
```

## 📖 Usage

Run the script and follow the interactive prompts:

```bash
python3 bootstrap.py
```

### Step-by-Step Process:

1. **Enter your project name**
2. **Select a programming language** (1-9)
3. **Choose a license** (1-5)
4. **Configure optional folders** (src/, tests/)
5. **Decide on git initialization**

### Example Output:

```
✅ Project Created!

Name: my-awesome-project
Language: Python
License: MIT

Created:

my-awesome-project/
├── README.md
├── .gitignore
├── LICENSE
├── src/ (optional)
├── tests/ (optional)
└── my_awesome_project.py

Happy coding 🚀
```

## 🛠️ Supported Languages

| Number | Language     | Extension | Starter File          |
|--------|--------------|-----------|-----------------------|
| 1      | Python       | `.py`     | `project_name.py`     |
| 2      | JavaScript   | `.js`     | `project_name.js`     |
| 3      | Java         | `.java`   | `ProjectName.java`    |
| 4      | C#           | `.cs`     | `Program.cs`          |
| 5      | C++          | `.cpp`    | `project_name.cpp`    |
| 6      | C            | `.c`      | `project_name.c`      |
| 7      | TypeScript   | `.ts`     | `project_name.ts`     |
| 8      | Go           | `.go`     | `project_name.go`     |
| 9      | Rust         | `.rs`     | `main.rs`             |

## 📄 Supported Licenses

| Number | License        | Description                                  |
|--------|----------------|----------------------------------------------|
| 1      | MIT            | Permissive, simple and permissive            |
| 2      | Apache 2.0     | Permissive with patent protection            |
| 3      | BSD 3-Clause   | Permissive with attribution requirement      |
| 4      | GPL v3         | Copyleft, requires sharing source            |
| 5      | None           | No license included                          |

## 📁 Project Structure

When you create a project, you'll get:

```
your-project-name/
├── README.md             # Project description and info
├── .gitignore            # Language-specific ignore rules
├── LICENSE               # Your chosen license (if selected)
├── src/                  # Optional source directory
│   └── your-project-name.ext
├── tests/                # Optional test directory
└── your-project-name.ext # Main source file (if not using src/)
```

## 💡 Examples

### Create a Python web scraper project:
```bash
python3 bootstrap.py
# Follow prompts: 
# Project name: web-scraper
# Language: 1 (Python)
# License: 1 (MIT)
# Src folder: y
# Tests folder: y
# Git init: y
```

### Create a Rust CLI tool:
```bash
python3 bootstrap.py
# Project name: cli-tool
# Language: 9 (Rust)
# License: 2 (Apache 2.0)
# Src folder: n
# Tests folder: y
# Git init: n
```

## 🔧 Customization

Want to customize the templates? Edit these sections in `bootstrap.py`:

- **Source file templates**: Look for the `templates` dictionary in `create_source_file()`
- **README template**: Modify the `create_readme()` function
- **Gitignore templates**: Adjust the `ignores` dictionary in `create_gitignore()`
- **License templates**: Update the `licenses` dictionary in `create_license()`

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- Inspired by various project generators and bootstrappers
- Built with ❤️ by Hexarion using Python's standard library
- Special thanks to the open-source community for inspiration

---

**Happy coding!** 🚀 Create amazing projects faster than ever before.
