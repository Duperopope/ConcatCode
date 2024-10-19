import sys
import os
import shutil
import zipfile
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QComboBox,
    QMessageBox, QFileDialog, QWidget, QVBoxLayout
)
from PyQt5.QtCore import Qt

class VersionManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set the window title and size
        self.setWindowTitle('Project Version Manager')
        self.setGeometry(200, 200, 400, 300)

        # General style using QSS (similar to CSS)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1b2a38;
            }
            QPushButton {
                background-color: #517fa4;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #243949;
            }
            QLabel {
                color: white;
                font-size: 18px;
                padding: 5px;
            }
            QComboBox {
                background-color: #ffffff;
                color: #000000;
                padding: 5px;
                font-size: 14px;
            }
        """)

        # Create a vertical layout for the interface elements
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Add a title label
        self.title_label = QLabel('Project Version Manager', self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Add buttons for different actions
        self.save_btn = QPushButton('Save Version', self)
        self.save_btn.clicked.connect(self.save_version)
        self.layout.addWidget(self.save_btn)

        self.restore_btn = QPushButton('Restore Version', self)
        self.restore_btn.clicked.connect(self.restore_version)
        self.layout.addWidget(self.restore_btn)

        self.archive_btn = QPushButton('Archive Version', self)
        self.archive_btn.clicked.connect(self.archive_version)
        self.layout.addWidget(self.archive_btn)

        self.extract_btn = QPushButton('Extract Version from ZIP', self)
        self.extract_btn.clicked.connect(self.extract_version)
        self.layout.addWidget(self.extract_btn)

    # Function to save a new version
    def save_version(self):
        try:
            self.concat_files_to_txt()
            QMessageBox.information(self, 'Success', 'New version saved successfully.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error while saving: {str(e)}')

    # Function to restore a version
    def restore_version(self):
        versions = self.get_versions_list()
        if not versions:
            QMessageBox.warning(self, 'No Versions', 'No versions available for restoration.')
            return

        version, ok = self.select_version(versions, "Restore")
        if ok:
            self.perform_restore(version)
            QMessageBox.information(self, 'Success', f'Version {version} restored successfully.')

    # Function to archive a version
    def archive_version(self):
        versions = self.get_versions_list()
        if not versions:
            QMessageBox.warning(self, 'No Versions', 'No versions available for archiving.')
            return

        version, ok = self.select_version(versions, "Archive")
        if ok:
            self.perform_archive(version)
            QMessageBox.information(self, 'Success', f'Version {version} archived successfully.')

    # Function to extract a version from a ZIP file
    def extract_version(self):
        zip_file, _ = QFileDialog.getOpenFileName(self, 'Choose a ZIP file', '', 'ZIP Files (*.zip)')
        if zip_file:
            self.perform_extract(zip_file)
            QMessageBox.information(self, 'Success', 'Files extracted successfully.')

    # Utility function to select a version from available versions
    def select_version(self, versions, action_name):
        combo = QComboBox(self)
        combo.addItems(versions)

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(f"{action_name} a Version")
        msg_box.setText("Select a version:")
        msg_box.layout().addWidget(combo)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.addButton(QMessageBox.Cancel)

        result = msg_box.exec_()

        if result == QMessageBox.Ok:
            return combo.currentText(), True
        return None, False

    # Function to get a list of available versions
    def get_versions_list(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        versions = [folder for folder in os.listdir(script_dir) if folder.startswith('version_')]
        return versions

    # Function to concatenate code files into a single text file
    def concat_files_to_txt(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version = self.get_next_version(script_dir)
        project_dir = os.path.abspath(os.path.join(script_dir, '..'))

        version_folder = os.path.join(script_dir, f"version_{version}_{current_datetime}")
        os.makedirs(version_folder, exist_ok=True)

        source_copy_folder = os.path.join(version_folder, "Source")
        os.makedirs(source_copy_folder, exist_ok=True)

        output_file = os.path.join(version_folder, f"concat_files_v{version}_{current_datetime}.txt")

        # Write header information to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"// Version: {version}\n")
            outfile.write(f"// Date: {current_datetime}\n")
            outfile.write("=" * 50 + "\n")

        # File extensions to process (common programming languages)
        extensions = (
            '.py', '.java', '.c', '.cpp', '.cs', '.js', '.ts',
            '.html', '.css', '.php', '.rb', '.go', '.swift', '.kt', '.rs'
        )

        # Walk through the project directory and process files
        for foldername, subfolders, filenames in os.walk(project_dir):
            for filename in filenames:
                if filename.endswith(extensions):
                    file_path = os.path.join(foldername, filename)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                        with open(output_file, 'a', encoding='utf-8') as outfile:
                            outfile.write(f"\n// File: {filename}\n")
                            outfile.write(infile.read())
                            outfile.write("\n" + "=" * 50 + "\n")

                    destination_file = os.path.join(source_copy_folder, f"{filename}.txt")
                    shutil.copy(file_path, destination_file)

        # Create a ZIP backup of the project
        zip_file_name = os.path.join(version_folder, f"backup_project_v{version}_{current_datetime}.zip")
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
            for foldername, subfolders, filenames in os.walk(project_dir):
                for filename in filenames:
                    if not filename.endswith('.zip') and 'version_' not in foldername:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, project_dir)
                        backup_zip.write(file_path, arcname)

    # Function to get the next available version number
    def get_next_version(self, script_dir):
        version_folders = [folder for folder in os.listdir(script_dir) if folder.startswith('version_')]
        versions = []
        for folder in version_folders:
            try:
                version_str = folder.split('_')[1]
                versions.append(float(version_str))
            except (IndexError, ValueError):
                continue

        if not versions:
            return "0.01"
        return f"{max(versions) + 0.01:.2f}"

    # Function to restore a version
    def perform_restore(self, version):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version_folder = os.path.join(script_dir, version)
        project_dir = os.path.abspath(os.path.join(script_dir, '..'))
        source_copy_folder = os.path.join(version_folder, "Source")

        # Restore each file from the version's source copy
        for foldername, subfolders, filenames in os.walk(source_copy_folder):
            for filename in filenames:
                source_file = os.path.join(foldername, filename)
                dest_file = os.path.join(project_dir, filename.replace(".txt", ""))
                shutil.copy(source_file, dest_file)

    # Function to archive a version
    def perform_archive(self, version):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version_folder = os.path.join(script_dir, version)
        archive_folder = os.path.join(script_dir, "Archived_Versions")
        os.makedirs(archive_folder, exist_ok=True)
        archive_path = os.path.join(archive_folder, f"{version}.zip")
        shutil.make_archive(archive_path.replace('.zip', ''), 'zip', version_folder)
        shutil.rmtree(version_folder)

    # Function to extract a version from a ZIP file
    def perform_extract(self, zip_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        extract_folder = os.path.join(script_dir, "extracted_version")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VersionManagerApp()
    window.show()
    sys.exit(app.exec_())
