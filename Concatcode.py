import sys
import os
import shutil
import zipfile
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QMessageBox, QFileDialog, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class VersionManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Gestion des Versions du Projet')
        self.setGeometry(200, 200, 400, 300)

        # Style général de l'interface avec QSS (similaire à CSS)
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

        # Créer un layout vertical pour les éléments de l'interface
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Ajouter un titre
        self.title_label = QLabel('Gestion des Versions du Projet', self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Ajouter les boutons
        self.sauvegarder_btn = QPushButton('Sauvegarder la version', self)
        self.sauvegarder_btn.clicked.connect(self.sauvegarder_version)
        self.layout.addWidget(self.sauvegarder_btn)

        self.restaurer_btn = QPushButton('Restaurer une version', self)
        self.restaurer_btn.clicked.connect(self.restaurer_version)
        self.layout.addWidget(self.restaurer_btn)

        self.archiver_btn = QPushButton('Archiver une version', self)
        self.archiver_btn.clicked.connect(self.archiver_version)
        self.layout.addWidget(self.archiver_btn)

        self.extraire_btn = QPushButton('Extraire une version d\'un ZIP', self)
        self.extraire_btn.clicked.connect(self.extraire_version)
        self.layout.addWidget(self.extraire_btn)

    # Fonction pour sauvegarder une nouvelle version
    def sauvegarder_version(self):
        try:
            self.concat_cs_files_to_txt()
            QMessageBox.information(self, 'Succès', 'Nouvelle version sauvegardée avec succès.')
        except Exception as e:
            QMessageBox.critical(self, 'Erreur', f'Erreur lors de la sauvegarde : {str(e)}')

    # Fonction pour restaurer une version
    def restaurer_version(self):
        versions = self.get_versions_list()
        if not versions:
            QMessageBox.warning(self, 'Aucune version', 'Aucune version disponible pour restauration.')
            return

        version, ok = self.select_version(versions, "Restaurer")
        if ok:
            self.restore_version(version)
            QMessageBox.information(self, 'Succès', f'Version {version} restaurée avec succès.')

    # Fonction pour archiver une version
    def archiver_version(self):
        versions = self.get_versions_list()
        if not versions:
            QMessageBox.warning(self, 'Aucune version', 'Aucune version disponible pour archivage.')
            return

        version, ok = self.select_version(versions, "Archiver")
        if ok:
            self.archive_version(version)
            QMessageBox.information(self, 'Succès', f'Version {version} archivée avec succès.')

    # Fonction pour extraire une version à partir d'un fichier ZIP
    def extraire_version(self):
        zip_file, _ = QFileDialog.getOpenFileName(self, 'Choisir un fichier ZIP', '', 'Fichiers ZIP (*.zip)')
        if zip_file:
            self.extract_version(zip_file)
            QMessageBox.information(self, 'Succès', 'Fichiers extraits avec succès.')

    # Utilitaire pour sélectionner une version
    def select_version(self, versions, action_name):
        combo = QComboBox(self)
        combo.addItems(versions)

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(action_name + " une version")
        msg_box.setText("Sélectionnez une version :")
        msg_box.layout().addWidget(combo)
        msg_box.addButton(QMessageBox.Ok)
        msg_box.addButton(QMessageBox.Cancel)

        result = msg_box.exec_()

        if result == QMessageBox.Ok:
            return combo.currentText(), True
        return None, False

    # Liste des versions disponibles
    def get_versions_list(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        versions = [folder for folder in os.listdir(script_dir) if folder.startswith('version_')]
        return versions

    # Fonction de sauvegarde (similaire au code précédent)
    def concat_cs_files_to_txt(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version = self.get_next_version(script_dir)
        project_dir = os.path.abspath(os.path.join(script_dir, '..'))

        version_folder = os.path.join(script_dir, f"version_{version}_{current_datetime}")
        os.makedirs(version_folder, exist_ok=True)

        source_copy_folder = os.path.join(version_folder, "Source")
        os.makedirs(source_copy_folder, exist_ok=True)

        output_file = os.path.join(version_folder, f"concat_files_v{version}_{current_datetime}.txt")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"// Version: {version}\n")
            outfile.write(f"// Date: {current_datetime}\n")
            outfile.write("=" * 50 + "\n")

        for foldername, subfolders, filenames in os.walk(project_dir):
            for filename in filenames:
                if filename.endswith(".cs"):
                    file_path = os.path.join(foldername, filename)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        with open(output_file, 'a', encoding='utf-8') as outfile:
                            outfile.write(f"\n// File: {filename}\n")
                            outfile.write(infile.read())
                            outfile.write("\n" + "=" * 50 + "\n")

                    destination_file = os.path.join(source_copy_folder, f"{filename}.txt")
                    shutil.copy(file_path, destination_file)

        zip_file_name = os.path.join(version_folder, f"backup_project_v{version}_{current_datetime}.zip")
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
            for foldername, subfolders, filenames in os.walk(project_dir):
                for filename in filenames:
                    if not filename.endswith('.zip') and 'version_' not in foldername:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, project_dir)
                        backup_zip.write(file_path, arcname)

    # Fonction pour obtenir la prochaine version disponible
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

    # Fonction pour restaurer une version
    def restore_version(self, version):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version_folder = os.path.join(script_dir, version)
        project_dir = os.path.abspath(os.path.join(script_dir, '..'))
        for foldername, subfolders, filenames in os.walk(version_folder):
            for filename in filenames:
                source_file = os.path.join(foldername, filename)
                dest_file = os.path.join(project_dir, filename.replace(".txt", ""))
                shutil.copy(source_file, dest_file)

    # Fonction pour archiver une version
    def archive_version(self, version):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version_folder = os.path.join(script_dir, version)
        archive_folder = os.path.join(script_dir, "Archived_Versions")
        os.makedirs(archive_folder, exist_ok=True)
        archive_path = os.path.join(archive_folder, f"{version}.zip")
        shutil.make_archive(archive_path.replace('.zip', ''), 'zip', version_folder)
        shutil.rmtree(version_folder)

    # Fonction pour extraire une version d'un fichier ZIP
    def extract_version(self, zip_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        extract_folder = os.path.join(script_dir, "extracted_version")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VersionManagerApp()
    window.show()
    sys.exit(app.exec_())
