Absolutely! Below is your updated `README.md` for **Project Version Manager**, now including a **Buy Me a Coffee** section to allow users to support you. Additionally, a **Buy Me a Coffee** badge has been added for greater visibility.

---

# 🚀 Project Version Manager: Your Ultimate GUI Tool for Efficient Version Control 🚀

**[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)**  
**[![GitHub Releases](https://img.shields.io/github/v/release/Duperopope/ProjectVersionManager)](https://github.com/Duperopope/ProjectVersionManager/releases)**  
**[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/samirmedjaher)**

Hello Reddit community!

I'm excited to introduce **Project Version Manager**, an open-source GUI application designed to simplify and enhance your project versioning and backup management. Whether you're a developer, writer, designer, or anyone managing multiple versions of files, this tool is tailored to meet your needs.

---

## 📌 Table of Contents

- [🌟 Features](#-features)
- [🔧 Installation](#-installation)
  - [📝 Prerequisites](#-prerequisites)
  - [🛠️ Setting Up the Environment](#-setting-up-the-environment)
  - [📦 Installing Dependencies](#-installing-dependencies)
- [📥 Download](#-download)
- [🛠️ Usage](#️-usage)
  - [🖥️ Application Overview](#🖥️-application-overview)
- [⚙️ Building Executables](#️-building-executables)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📫 Contact](#-contact)
- [☕ Support](#-support)

---

## 🌟 Features

- **Save Version:** Capture the current state of your project by saving all relevant source files into a single text file and creating a ZIP backup.
- **Restore Version:** Easily revert your project to any previously saved version.
- **Archive Version:** Compress and archive specific versions for long-term storage.
- **Extract Version from ZIP:** Extract project versions from existing ZIP files seamlessly.
- **User-Friendly GUI:** Built with PyQt5, offering an intuitive interface for effortless navigation and operation.
- **Cross-Platform Support:** Available as a Windows `.exe` for easy installation and use.

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

## 📥 Download

### **Windows Executable (.exe)**

For Windows users, a pre-built executable is available for easy installation without the need to set up a Python environment.

1. **Navigate to the [Releases Page](https://github.com/Duperopope/ProjectVersionManager/releases).**

2. **Download the Latest `.exe` File:**

   - Look for the latest release (e.g., `v1.0.0`) and download the `ProjectVersionManager.exe` file.

   ![Download Executable](https://your-image-link.com/download-exec.png)  
   *(Replace with an actual screenshot of the Releases page)*

3. **Run the Executable:**

   - After downloading, double-click `ProjectVersionManager.exe` to launch the application.

   **Note:** If you encounter a security warning, right-click the executable, select **Properties**, and click **Run Anyway**.

---

## 🛠️ Usage

After installation or downloading the executable, launch **Project Version Manager**.

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
  pyinstaller --onefile --windowed Concatcode.py --add-data "path/to/datafile;destination_folder"
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
   - Click the "Fork" button on the [repository page](https://github.com/Duperopope/ProjectVersionManager).

2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/Duperopope/ProjectVersionManager.git
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

## ☕ Support

If you find **Project Version Manager** helpful and would like to support its development, consider buying me a coffee! Your support helps in maintaining and improving the project.

**[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/samirmedjaher)**

---

Thank you for checking out **Project Version Manager**! Your support and feedback are invaluable in making this tool even better. Happy versioning! 🎉

---

**[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://opensource.org/) [![GitHub Stars](https://img.shields.io/github/stars/Duperopope/ProjectVersionManager?style=social)](https://github.com/Duperopope/ProjectVersionManager)**

---

Feel free to share your thoughts, ask questions, or suggest improvements in the comments below!

---

## 📤 How to Upload the `.exe` to GitHub Releases

To make the Windows executable (`.exe`) available for download directly from GitHub Releases, follow these steps:

1. **Build the Executable:**
   - Ensure you've built the `.exe` using PyInstaller as outlined in the [Building Executables](#️-building-executables) section.

2. **Navigate to Your Repository on GitHub:**
   - Go to [https://github.com/Duperopope/ProjectVersionManager](https://github.com/Duperopope/ProjectVersionManager).

3. **Go to the Releases Page:**
   - Click on the **"Releases"** section on the right sidebar or navigate to [https://github.com/Duperopope/ProjectVersionManager/releases](https://github.com/Duperopope/ProjectVersionManager/releases).

4. **Create a New Release:**
   - Click on the **"Draft a new release"** button.

5. **Fill in Release Details:**
   - **Tag version:** Use a semantic versioning tag (e.g., `v1.0.0`).
   - **Release title:** Provide a descriptive title (e.g., `v1.0.0 - Initial Release`).
   - **Description:** Summarize the release notes or changes.

6. **Upload the Executable:**
   - Under **"Attach binaries by dropping them here or selecting them."**, drag and drop your `ProjectVersionManager.exe` file or click to browse and select it.

   ![Upload Executable](https://your-image-link.com/upload-exec.png)  
   *(Replace with an actual screenshot if available)*

7. **Publish the Release:**
   - Once the `.exe` is uploaded and all details are filled, click **"Publish release"**.

8. **Verify the Release:**
   - After publishing, the release page will display the `.exe` file as a downloadable asset.

   ![Published Release](https://your-image-link.com/published-release.png)  
   *(Replace with an actual screenshot if available)*

9. **Update the README:**
   - Ensure the **[Download](#-download)** section of your `README.md` points users to the latest release for downloading the `.exe`.

   **Example Link in README:**

   ```markdown
   [Download the Latest Windows Executable](https://github.com/Duperopope/ProjectVersionManager/releases/latest/download/ProjectVersionManager.exe)
   ```

   **Note:** Replace `ProjectVersionManager.exe` with your actual executable file name if different.

---

By following these steps, users will be able to easily download and install **Project Version Manager** on their Windows systems without the need to set up a Python environment. This enhances the accessibility and user experience of your application.

If you have any further questions or need assistance with the release process, feel free to ask!

---

**🔗 Useful Links:**

- [GitHub Repository](https://github.com/Duperopope/ProjectVersionManager)
- [PyInstaller Documentation](https://pyinstaller.readthedocs.io/en/stable/)
- [Official Python Website](https://www.python.org/)

---

Feel free to customize further as needed! If you have any more requests or need additional modifications, let me know.
