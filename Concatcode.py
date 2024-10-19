import sys
import os
import shutil
import zipfile
import logging

from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QComboBox,
    QMessageBox, QFileDialog, QWidget, QVBoxLayout, QDialog,
    QDialogButtonBox, QHBoxLayout
)
from PyQt5.QtCore import Qt

# Configure logging
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class VersionSelectionDialog(QDialog):
    """
    A custom dialog for selecting a version from a list.
    """

    def __init__(self, versions, action_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{action_name} a Version")
        self.setModal(True)
        self.selected_version = None
        self.init_ui(versions, action_name)

    def init_ui(self, versions, action_name):
        layout = QVBoxLayout()

        label = QLabel(f"Please select a version to {action_name.lower()}:")
        layout.addWidget(label)

        self.combo = QComboBox()
        self.combo.addItems(versions)
        layout.addWidget(self.combo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_selected_version(self):
        if self.exec_() == QDialog.Accepted:
            return self.combo.currentText()
        return None

class VersionManagerApp(QMainWindow):
    """
    A GUI application for managing project versions.
    Allows users to save, restore, archive, and extract versions of their project.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface components.
        """
        # Set the window title and size
        self.setWindowTitle('Project Version Manager')
        self.setGeometry(200, 200, 500, 400)

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

    def show_error_dialog(self, title, message):
        """
        Utility method to show an error dialog with options to open the log file.

        Parameters:
            title (str): The title of the error dialog.
            message (str): The main error message.
        """
        # Log the detailed error with traceback
        logging.error(message)

        # Get absolute path to error.log
        script_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(script_dir, 'error.log')

        # Create a critical message box
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setInformativeText(f"Please check the error log here:\n{log_file_path}")

        # Add buttons
        open_log_btn = msg_box.addButton('Open Log', QMessageBox.AcceptRole)
        close_btn = msg_box.addButton('Close', QMessageBox.RejectRole)

        # Execute the message box
        msg_box.exec_()

        # Handle button clicks
        if msg_box.clickedButton() == open_log_btn:
            try:
                if sys.platform.startswith('darwin'):
                    os.system(f'open "{log_file_path}"')
                elif os.name == 'nt':
                    os.startfile(log_file_path)
                elif os.name == 'posix':
                    os.system(f'xdg-open "{log_file_path}"')
            except Exception as open_e:
                logging.error("Failed to open error log.", exc_info=True)
                QMessageBox.critical(
                    self,
                    'Log Open Error',
                    f'Failed to open the error log file:\n{str(open_e)}'
                )

    def show_success_dialog(self, title, message, details=None):
        """
        Utility method to show a success dialog with optional details.

        Parameters:
            title (str): The title of the success dialog.
            message (str): The main success message.
            details (str, optional): Additional details to display.
        """
        # Create an information message box
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        if details:
            msg_box.setDetailedText(details)

        msg_box.addButton('OK', QMessageBox.AcceptRole)
        msg_box.exec_()

    def save_version(self):
        """
        Function to save a new version of the project.
        """
        try:
            version_info = self.concat_files_to_txt()
            success_message = 'New version saved successfully.'
            details = (
                f"Version: {version_info['version']}\n"
                f"Date: {version_info['datetime']}\n"
                f"Version Folder: {version_info['version_folder']}\n"
                f"Backup ZIP: {version_info['zip_file']}"
            )
            self.show_success_dialog('Success', success_message, details)
        except Exception as e:
            self.show_error_dialog(
                title='Save Error',
                message=f'An error occurred while saving the version:\n{str(e)}'
            )

    def restore_version(self):
        """
        Function to restore a previously saved version.
        """
        try:
            versions = self.get_versions_list()
            if not versions:
                QMessageBox.warning(self, 'No Versions', 'No versions available for restoration.')
                return

            dialog = VersionSelectionDialog(versions, "Restore", self)
            selected_version = dialog.get_selected_version()
            if selected_version:
                self.perform_restore(selected_version)
                success_message = f'Version {selected_version} restored successfully.'
                details = f"Version: {selected_version}\nRestored to project directory."
                self.show_success_dialog('Success', success_message, details)
        except Exception as e:
            self.show_error_dialog(
                title='Restore Error',
                message=f'An error occurred while restoring the version:\n{str(e)}'
            )

    def archive_version(self):
        """
        Function to archive a saved version.
        """
        try:
            versions = self.get_versions_list()
            if not versions:
                QMessageBox.warning(self, 'No Versions', 'No versions available for archiving.')
                return

            dialog = VersionSelectionDialog(versions, "Archive", self)
            selected_version = dialog.get_selected_version()
            if selected_version:
                self.perform_archive(selected_version)
                success_message = f'Version {selected_version} archived successfully.'
                details = f"Version: {selected_version}\nArchived to 'Archived_Versions' folder."
                self.show_success_dialog('Success', success_message, details)
        except Exception as e:
            self.show_error_dialog(
                title='Archive Error',
                message=f'An error occurred while archiving the version:\n{str(e)}'
            )

    def extract_version(self):
        """
        Function to extract a version from a ZIP file.
        """
        try:
            zip_file, _ = QFileDialog.getOpenFileName(self, 'Choose a ZIP file', '', 'ZIP Files (*.zip)')
            if zip_file:
                extract_info = self.perform_extract(zip_file)
                success_message = 'Files extracted successfully.'
                details = (
                    f"ZIP File: {zip_file}\n"
                    f"Extracted to: {extract_info['extract_folder']}"
                )
                self.show_success_dialog('Success', success_message, details)
        except Exception as e:
            self.show_error_dialog(
                title='Extract Error',
                message=f'An error occurred while extracting the version from ZIP:\n{str(e)}'
            )

    def get_versions_list(self):
        """
        Function to get a list of available versions.

        Returns:
            list: A list of version folder names.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        versions = [folder for folder in os.listdir(script_dir) if folder.startswith('version_')]
        return versions

    def concat_files_to_txt(self):
        """
        Function to concatenate code files into a single text file.
        Saves the concatenated file and a backup ZIP of the project.

        Returns:
            dict: Information about the saved version.
        """
        try:
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
            for foldername, subfolders, filenames in os.walk(project_dir, topdown=True):
                # Exclude version folders and Archived_Versions from being processed
                excluded_dirs = [d for d in subfolders if d.startswith('version_') or d == 'Archived_Versions']
                for d in excluded_dirs:
                    subfolders.remove(d)  # This will prevent os.walk from traversing into these directories

                for filename in filenames:
                    if filename.endswith(extensions):
                        file_path = os.path.join(foldername, filename)
                        destination_file = os.path.join(source_copy_folder, filename)

                        # Prevent copying the script itself
                        if os.path.abspath(file_path) == os.path.abspath(__file__):
                            continue

                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                                with open(output_file, 'a', encoding='utf-8') as outfile:
                                    outfile.write(f"\n// File: {filename}\n")
                                    outfile.write(infile.read())
                                    outfile.write("\n" + "=" * 50 + "\n")
                        except Exception as read_e:
                            logging.error(f"Failed to read file {file_path}.", exc_info=True)
                            continue  # Skip this file and continue with others

                        try:
                            shutil.copy(file_path, destination_file)
                        except shutil.SameFileError:
                            logging.error(f"Attempted to copy the same file: {file_path}", exc_info=True)
                            continue  # Skip copying this file
                        except Exception as copy_e:
                            logging.error(f"Failed to copy file {file_path} to {destination_file}.", exc_info=True)
                            continue  # Skip copying this file

            # Create a ZIP backup of the project
            zip_file_name = os.path.join(version_folder, f"backup_project_v{version}_{current_datetime}.zip")
            try:
                with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
                    for foldername, subfolders, filenames in os.walk(project_dir, topdown=True):
                        # Exclude version folders and Archived_Versions from being zipped
                        excluded_dirs = [d for d in subfolders if d.startswith('version_') or d == 'Archived_Versions']
                        for d in excluded_dirs:
                            subfolders.remove(d)  # Prevent os.walk from traversing into these directories

                        for filename in filenames:
                            if filename.endswith('.zip'):
                                continue  # Exclude existing zip files
                            file_path = os.path.join(foldername, filename)
                            arcname = os.path.relpath(file_path, project_dir)

                            # Prevent zipping the script itself
                            if os.path.abspath(file_path) == os.path.abspath(__file__):
                                continue

                            backup_zip.write(file_path, arcname)
            except Exception as zip_e:
                logging.error(f"Failed to create ZIP backup: {zip_file_name}.", exc_info=True)
                raise zip_e  # Re-raise to be caught by the caller

            # Return version information for the success dialog
            return {
                'version': version,
                'datetime': current_datetime,
                'version_folder': version_folder,
                'zip_file': zip_file_name
            }

        except Exception as e:
            logging.error("Failed to concatenate and backup files.", exc_info=True)
            raise e  # Re-raise the exception to be caught by the caller

    def get_next_version(self, script_dir):
        """
        Function to get the next available version number.

        Parameters:
            script_dir (str): The directory where the script is located.

        Returns:
            str: The next version number as a string.
        """
        version_folders = [folder for folder in os.listdir(script_dir) if folder.startswith('version_')]
        versions = []
        for folder in version_folders:
            try:
                # Extract the version number from the folder name
                version_str = folder.split('_')[1]
                versions.append(float(version_str))
            except (IndexError, ValueError):
                continue

        if not versions:
            return "0.01"
        return f"{max(versions) + 0.01:.2f}"

    def perform_restore(self, version):
        """
        Function to restore a version.

        Parameters:
            version (str): The name of the version folder to restore.
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            version_folder = os.path.join(script_dir, version)
            project_dir = os.path.abspath(os.path.join(script_dir, '..'))
            source_copy_folder = os.path.join(version_folder, "Source")

            # Restore each file from the version's source copy
            for foldername, subfolders, filenames in os.walk(source_copy_folder):
                for filename in filenames:
                    source_file = os.path.join(foldername, filename)
                    dest_file = os.path.join(project_dir, filename)

                    # Prevent copying the script itself
                    if os.path.abspath(source_file) == os.path.abspath(__file__):
                        continue

                    try:
                        shutil.copy(source_file, dest_file)
                    except Exception as copy_e:
                        logging.error(f"Failed to copy file {source_file} to {dest_file}.", exc_info=True)
                        continue  # Skip copying this file
        except Exception as e:
            logging.error("Failed to restore version.", exc_info=True)
            raise e  # Re-raise to be caught by the caller

    def perform_archive(self, version):
        """
        Function to archive a version.

        Parameters:
            version (str): The name of the version folder to archive.
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            version_folder = os.path.join(script_dir, version)
            archive_folder = os.path.join(script_dir, "Archived_Versions")
            os.makedirs(archive_folder, exist_ok=True)
            archive_base_name = os.path.join(archive_folder, version)
            shutil.make_archive(archive_base_name, 'zip', root_dir=version_folder)
            shutil.rmtree(version_folder)
        except Exception as e:
            logging.error("Failed to archive version.", exc_info=True)
            raise e  # Re-raise to be caught by the caller

    def perform_extract(self, zip_file):
        """
        Function to extract a version from a ZIP file.

        Parameters:
            zip_file (str): The path to the ZIP file to extract.

        Returns:
            dict: Information about the extraction.
        """
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            extract_folder = os.path.join(script_dir, "extracted_version", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
            os.makedirs(extract_folder, exist_ok=True)
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            return {'extract_folder': extract_folder}
        except Exception as e:
            logging.error("Failed to extract version from ZIP.", exc_info=True)
            raise e  # Re-raise to be caught by the caller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VersionManagerApp()
    window.show()
    sys.exit(app.exec_())
