# Project Version Manager

A desktop application to manage versions of your projects by saving, restoring, archiving, and extracting code files across multiple programming languages.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Saving a Version](#saving-a-version)
  - [Restoring a Version](#restoring-a-version)
  - [Archiving a Version](#archiving-a-version)
  - [Extracting a Version from ZIP](#extracting-a-version-from-zip)
- [Supported Languages](#supported-languages)
- [Building Executables](#building-executables)
  - [Windows](#windows)
  - [Linux](#linux)
  - [macOS](#macos)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Save Versions**: Save snapshots of your project, concatenating code files into a single text file.
- **Restore Versions**: Restore your project to a previously saved state.
- **Archive Versions**: Archive saved versions to save space.
- **Extract Versions**: Extract archived versions from ZIP files.
- **Multi-language Support**: Handles code files from multiple programming languages.

## Prerequisites

- **Python 3.6 or higher**
- **PyQt5**: For the graphical user interface.
- **PyInstaller**: (Optional) For building executables.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/project-version-manager.git
   cd project-version-manager
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not available, install manually:*

   ```bash
   pip install PyQt5
   ```

## Usage

Run the application using:

```bash
python version_manager.py
```

Replace `version_manager.py` with the name of your script if different.

### Application Interface

Upon launching, you'll see a window with the following options:

- **Save Version**: Saves the current state of your project.
- **Restore Version**: Restores your project to a selected saved version.
- **Archive Version**: Archives a saved version into a ZIP file and removes the original folder.
- **Extract Version from ZIP**: Extracts a version from a ZIP file.

### Directory Structure

- **Project Directory**: The parent directory of the script. The script assumes your project files are located one level up from where the script resides.
- **Version Folders**: Saved versions are stored in folders named `version_X.XX_YYYY-MM-DD_HH-MM-SS`.

### Saving a Version

1. Click **Save Version**.
2. The application will:
   - Concatenate all code files into a single text file.
   - Copy individual code files into a `Source` folder.
   - Create a ZIP backup of your project.
3. A success message will appear upon completion.

### Restoring a Version

1. Click **Restore Version**.
2. Select a version from the dropdown list.
3. Confirm your selection.
4. The application will overwrite the current project files with those from the selected version.

**Warning**: Restoring will overwrite existing files. Make sure to back up any unsaved changes.

### Archiving a Version

1. Click **Archive Version**.
2. Select a version from the dropdown list.
3. Confirm your selection.
4. The application will:
   - Create a ZIP archive of the selected version.
   - Move it to the `Archived_Versions` folder.
   - Delete the original version folder.

### Extracting a Version from ZIP

1. Click **Extract Version from ZIP**.
2. Browse and select the ZIP file you wish to extract.
3. The contents will be extracted to an `extracted_version` folder.

## Supported Languages

The application processes code files with the following extensions:

- Python (`.py`)
- Java (`.java`)
- C (`.c`)
- C++ (`.cpp`)
- C# (`.cs`)
- JavaScript (`.js`)
- TypeScript (`.ts`)
- HTML (`.html`)
- CSS (`.css`)
- PHP (`.php`)
- Ruby (`.rb`)
- Go (`.go`)
- Swift (`.swift`)
- Kotlin (`.kt`)
- Rust (`.rs`)

## Building Executables

You can create standalone executables for Windows, Linux, and macOS using PyInstaller.

### Install PyInstaller

```bash
pip install pyinstaller
```

### Windows

1. **Build the Executable**:

   ```bash
   pyinstaller --onefile --windowed version_manager.py
   ```

2. **Locate the Executable**:

   The executable will be in the `dist` folder as `version_manager.exe`.

### Linux

1. **Build the Executable**:

   ```bash
   pyinstaller --onefile --windowed version_manager.py
   ```

2. **Make Executable**:

   ```bash
   chmod +x dist/version_manager
   ```

3. **Run the Executable**:

   ```bash
   ./dist/version_manager
   ```

### macOS

1. **Build the Executable**:

   ```bash
   pyinstaller --onefile --windowed version_manager.py
   ```

2. **Locate the Application**:

   The application bundle will be in the `dist` folder.

**Note**: PyInstaller must be run on the target operating system to build the executable for that system.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.

---

**Disclaimer**: This tool is intended for basic version management and should not replace full-fledged version control systems like Git.

# How to Use the Project Version Manager

## Introduction

The Project Version Manager is a user-friendly application designed to help you manage different versions of your project code. It's especially useful for small projects or individual developers who need a simple way to keep track of code changes without the complexity of a full version control system.

## Step-by-Step Guide

### 1. Preparing Your Environment

- **Ensure that your project is organized**: The script assumes that your project files are located in the parent directory relative to where the script is placed.
- **Check your files**: The application will process code files with extensions listed in the [Supported Languages](#supported-languages) section.

### 2. Launching the Application

- Run the application using:

  ```bash
  python version_manager.py
  ```

- Alternatively, if you've built an executable, double-click the executable file.

### 3. Saving a Version

- Click on **Save Version**.
- The application will automatically:
  - Generate a new version number.
  - Concatenate all code files into a single text file for easy viewing.
  - Copy individual code files into a `Source` folder within the version folder.
  - Create a ZIP backup of your entire project.
- A confirmation message will appear once the process is complete.

### 4. Restoring a Version

- Click on **Restore Version**.
- A dialog will appear with a dropdown menu of available versions.
- Select the version you wish to restore and click **OK**.
- The application will overwrite the current project files with those from the selected version.
- **Important**: Ensure you've backed up any unsaved changes before restoring.

### 5. Archiving a Version

- Click on **Archive Version**.
- Select the version you wish to archive from the dropdown menu and click **OK**.
- The application will:
  - Create a ZIP archive of the selected version.
  - Move the archive to the `Archived_Versions` folder.
  - Delete the original version folder to save space.
- A confirmation message will appear upon completion.

### 6. Extracting a Version from ZIP

- Click on **Extract Version from ZIP**.
- Browse to the ZIP file you want to extract and select it.
- The contents will be extracted to a folder named `extracted_version`.
- You can then manually move or copy these files to your project directory as needed.

## Tips and Best Practices

- **Regular Saves**: Save versions regularly, especially before making significant changes.
- **Archiving**: Archive older versions to keep your working directory clean and save disk space.
- **Backup**: Although the application creates backups, it's good practice to maintain additional backups of your project.

## Troubleshooting

- **No Versions Available**: If you try to restore or archive and no versions are listed, ensure you've saved at least one version.
- **File Overwrites**: Restoring a version will overwrite current files. Always back up current work if unsure.
- **Permission Errors**: If you encounter permission issues, try running the application with administrative privileges.

## Contact

If you have any questions or need support, please contact [your.email@example.com](mailto:your.s.medjaher@gmail.com).

---
