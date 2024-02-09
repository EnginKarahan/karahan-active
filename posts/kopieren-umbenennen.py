import os
import shutil
import logging
from datetime import datetime


def copy_files_and_rename(directory_source, directory_destination):
    # Überprüfe, ob das Quellverzeichnis existiert
    if not os.path.exists(directory_source):
        print(f"Das Quellverzeichnis '{directory_source}' existiert nicht.")
        return

    # Überprüfe, ob das Zielverzeichnis existiert
    if not os.path.exists(directory_destination):
        print(f"Das Zielverzeichnis '{directory_destination}' existiert nicht.")
        return

    # Konstruiere den Dateinamen für die Logdatei basierend auf dem aktuellen Datum und der Uhrzeit
    log_filename = datetime.now().strftime("%Y%m%d%H%M.log")

    # Konfiguriere das Logging
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

    # Liste alle Dateien im Quellverzeichnis auf
    files = [f for f in os.listdir(directory_source) if os.path.isfile(os.path.join(directory_source, f)) and f.endswith('.md')]

    for file in files:
        # Entferne die Endung ".md" vom Dateinamen
        folder_name = os.path.splitext(file)[0]

        # Konstruiere den Pfad zur Quelldatei
        source_file_path = os.path.join(directory_source, file)

        # Konstruiere den Pfad zum Zielunterverzeichnis
        destination_subdirectory = os.path.join(directory_destination, folder_name)

        # Prüfe, ob das Zielunterverzeichnis bereits existiert
        if os.path.exists(destination_subdirectory):
            # Konstruiere den neuen Dateinamen (index.tr.md) für die Kopie
            new_file_name = 'index.tr.md'

            # Konstruiere den Pfad zur Ziel-Datei im Zielunterverzeichnis
            destination_file_path = os.path.join(destination_subdirectory, new_file_name)

            # Kopiere die Datei in das Zielunterverzeichnis und benenne sie um
            shutil.copy2(source_file_path, destination_file_path)

            # Logge die Aktion in die Logdatei
            logging.info(f"Datei '{file}' wurde erfolgreich in das Zielunterverzeichnis '{folder_name}' kopiert und umbenannt.")

            # Lösche die Quelldatei
            os.remove(source_file_path)
        else:
            # Erstelle ein neues Zielunterverzeichnis
            os.makedirs(destination_subdirectory, exist_ok=True)

            # Konstruiere den neuen Dateinamen (index.tr.md) für die Kopie
            new_file_name = 'index.tr.md'

            # Konstruiere den Pfad zur Ziel-Datei im Zielunterverzeichnis
            destination_file_path = os.path.join(destination_subdirectory, new_file_name)

            # Kopiere die Datei in das Zielunterverzeichnis und benenne sie um
            shutil.copy2(source_file_path, destination_file_path)

            # Logge die Aktion in die Logdatei
            logging.info(f"Datei '{file}' wurde erfolgreich in das neue Zielunterverzeichnis '{folder_name}' kopiert und umbenannt.")

            # Lösche die Quelldatei
            os.remove(source_file_path)

# Beispielaufruf
source_directory_path = '../tr/posts'
destination_directory_path = './'
copy_files_and_rename(source_directory_path, destination_directory_path)
