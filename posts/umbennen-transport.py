import os
import shutil
import logging
from datetime import datetime

def create_subdirectories_and_copy_files(directory):
    # Überprüfe, ob das Verzeichnis existiert
    if not os.path.exists(directory):
        print(f"Das Verzeichnis '{directory}' existiert nicht.")
        return

    # Konstruiere den Dateinamen für die Logdatei basierend auf dem aktuellen Datum und der Uhrzeit
    log_filename = datetime.now().strftime("%Y%m%d%H%M.log")

    # Konfiguriere das Logging
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

    # Liste alle Dateien im Verzeichnis auf
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.md')]

    # Iteriere über die Dateien und erstelle Unterverzeichnisse
    for file in files:
        # Entferne die Endung ".md" vom Dateinamen
        folder_name = os.path.splitext(file)[0]

        # Erstelle ein neues Unterverzeichnis
        new_directory = os.path.join(directory, folder_name)
        os.makedirs(new_directory, exist_ok=True)

        # Konstruiere den neuen Dateinamen (index.de.md) für die Kopie
        new_file_name = 'index.de.md'

        # Konstruiere den Pfad zur ursprünglichen Datei
        old_file_path = os.path.join(directory, file)

        # Konstruiere den Pfad zur neuen Datei im Unterverzeichnis
        new_file_path = os.path.join(new_directory, new_file_name)

        # Kopiere die Datei in das neue Unterverzeichnis und benenne sie um
        shutil.copy2(old_file_path, new_file_path)

        # Logge die Aktion in die Logdatei
        logging.info(f"Datei '{file}' wurde erfolgreich in das Unterverzeichnis '{folder_name}' kopiert und umbenannt.")

# Beispielaufruf
directory_path = './'
create_subdirectories_and_copy_files(directory_path)
