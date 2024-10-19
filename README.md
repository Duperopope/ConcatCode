# 🚀 Project Version Manager: Your Ultimate GUI Tool for Efficient Version Control 🚀

**[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)**

Hello Reddit community!

I'm excited to introduce **Project Version Manager**, an open-source GUI application designed to simplify and enhance your project versioning and backup management. Whether you're a developer, writer, designer, or anyone managing multiple versions of files, this tool is tailored to meet your needs.

---

## 📌 Table of Contents

- [🌟 Features](#-features)
- [🔧 Installation](#-installation)
- [🛠️ Usage](#️-usage)
- [⚙️ Building Executables](#️-building-executables)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📫 Contact](#-contact)

---

## 🌟 Features

- **Save Version:** Capture the current state of your project by saving all relevant source files into a single text file and creating a ZIP backup.
- **Restore Version:** Easily revert your project to any previously saved version.
- **Archive Version:** Compress and archive specific versions for long-term storage.
- **Extract Version from ZIP:** Extract project versions from existing ZIP files seamlessly.
- **User-Friendly GUI:** Built with PyQt5, offering an intuitive interface for effortless navigation and operation.

---

## 🔧 Installation

### 📝 Prerequisites

Ensure your system meets the following requirements:

- **Operating System:** Windows, Mac OS, or Linux.
- **Python:** Version 3.6 or higher.
- **pip:** Python package installer.

### 🛠️ Setting Up the Environment

It's recommended to use a virtual environment to manage dependencies:

1. **Install Python:**

   - **Windows & Mac OS:**
     - Download from the [official Python website](https://www.python.org/downloads/).
     - Run the installer and **ensure "Add Python to PATH" is checked**.

   - **Linux:**
     - Verify installation:
       ```bash
       python3 --version
       ```
     - If not installed, use your distribution's package manager. For example, on Ubuntu:
       ```bash
       sudo apt update
       sudo apt install python3 python3-venv python3-pip
       ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   cd /path/to/ProjectVersionManager
   python3 -m venv venv
   ```

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac OS & Linux:**
     ```bash
     source venv/bin/activate
     ```

   *(Your terminal should show `(venv)` indicating the environment is active.)*

### 📦 Installing Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

*If `requirements.txt` is unavailable:*

```bash
pip install PyQt5
```

---

## 🛠️ Usage

After installation, run the application with:

```bash
python Concatcode.py
```

**Note:** Ensure you're in the project directory and the virtual environment is active.

### 🖥️ Application Overview

- **Save Version:** Click to save the current project state.
- **Restore Version:** Select and restore from available versions.
- **Archive Version:** Choose a version to archive.
- **Extract Version from ZIP:** Import versions from existing ZIP files.

**User Interface:**

![GUI Screenshot](https://your-image-link.com/screenshot.png)

*(Replace with an actual screenshot of the application)*

---

## ⚙️ Building Executables

Distribute **Project Version Manager** without requiring users to install Python or dependencies using **PyInstaller**.

### 🛠️ Prerequisites

Install PyInstaller within your virtual environment:

```bash
pip install pyinstaller
```

### 🖥️ Building on Different OS

#### **Windows**

1. **Navigate to Project Directory:**
   ```bash
   cd C:\path\to\ProjectVersionManager
   ```

2. **Build Executable:**
   ```bash
   pyinstaller --onefile --windowed Concatcode.py
   ```

3. **Retrieve Executable:**
   - Located at `dist\Concatcode.exe`

4. **Run:**
   - Double-click `Concatcode.exe` to launch.

#### **Mac OS**

1. **Navigate to Project Directory:**
   ```bash
   cd /path/to/ProjectVersionManager
   ```

2. **Build Application Bundle:**
   ```bash
   pyinstaller --onefile --windowed Concatcode.py
   ```

3. **Retrieve Application:**
   - Located at `dist/Concatcode.app`

4. **Run:**
   - Double-click `Concatcode.app`

   *If blocked, right-click and select **Open**, then **Open** again in the dialog.*

#### **Linux**

1. **Navigate to Project Directory:**
   ```bash
   cd /path/to/ProjectVersionManager
   ```

2. **Build Executable:**
   ```bash
   pyinstaller --onefile Concatcode.py
   ```

3. **Retrieve Executable:**
   - Located at `dist/Concatcode`

4. **Set Permissions and Run:**
   ```bash
   chmod +x dist/Concatcode
   ./dist/Concatcode
   ```

### 🔍 Additional Tips

- **Include Additional Files:**
  ```bash
  pyinstaller --onefile --windowed Concatcode.py --add-data "path/to/datafile:destination_folder"
  ```
  - **Windows:** Use `;` as separator.
  - **Mac OS & Linux:** Use `:` as separator.

- **Handle Hidden Imports:**
  ```bash
  pyinstaller --onefile --windowed Concatcode.py --hidden-import module_name
  ```

- **Advanced Configurations:**
  - Modify the generated `.spec` file and rebuild:
    ```bash
    pyinstaller Concatcode.spec
    ```

---

## 🐛 Troubleshooting

### **Import Errors: PyQt5 Not Found**

**Error Message:**
```
Import "PyQt5.QtWidgets" could not be resolved Pylance reportMissingImports
```

**Solutions:**

1. **Install PyQt5:**
   ```bash
   pip install PyQt5
   ```

2. **Verify Installation:**
   ```bash
   python -c "import PyQt5"
   ```

3. **Configure Your IDE:**
   - **Visual Studio Code:**
     - Select the correct Python interpreter.
     - Restart VS Code.

4. **Restart Your IDE:**
   - Sometimes necessary to recognize new installations.

### **Executable Not Running**

**Possible Causes:**

- Missing dependencies.
- Incorrect build process.

**Solutions:**

1. **Rebuild Executable:**
   ```bash
   pyinstaller --onefile --windowed Concatcode.py
   ```

2. **Check Build Errors:**
   - Review terminal output for issues.

3. **Test in Development:**
   ```bash
   python Concatcode.py
   ```

4. **Include Hidden Imports:**
   ```bash
   pyinstaller --onefile --windowed Concatcode.py --hidden-import module_name
   ```

---

## 🤝 Contributing

Contributions are highly appreciated! Here's how you can contribute:

1. **Fork the Repository:**
   - Click the "Fork" button on the repository page.

2. **Clone Your Fork:**
   ```bash
  https://github.com/Duperopope/ConcatCode.git
   ```

3. **Create a New Branch:**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Implement Your Changes:**
   - Add features or fix bugs.

5. **Commit Your Changes:**
   ```bash
   git commit -m "Add your commit message"
   ```

6. **Push to Your Fork:**
   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request:**
   - Navigate to your fork and click "Compare & pull request".

**Please ensure your contributions follow the project's coding standards and include appropriate documentation and tests.**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📫 Contact

Developed by **Samir Medjaher**. If you have any questions, suggestions, or need support, feel free to reach out:

📧 **Email:** [s.medjaher@gmail.com](mailto:s.medjaher@gmail.com)

---

Thank you for checking out **Project Version Manager**! Your support and feedback are invaluable in making this tool even better. Happy versioning! 🎉

---

**[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://opensource.org/) [![GitHub Stars](https://img.shields.io/github/stars/your_username/ProjectVersionManager?style=social)](https://github.com/your_username/ProjectVersionManager)**

*(Replace `your_username` with your actual GitHub username and update links accordingly.)*

---

Feel free to share your thoughts, ask questions, or suggest improvements in the comments below!
