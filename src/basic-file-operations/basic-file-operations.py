from datetime import datetime
from pathlib import Path

script_location = Path(__file__).resolve()

print(f"Script location ABS path: {script_location}")

script_folder = script_location.parent

print(f"Script folder: {script_folder}")

path_cwd = Path.cwd()

print(f"Shell location: {path_cwd}")

deployment_file = "deployment.yaml"

deployment_file_abs_path = script_folder / deployment_file

deployment_exists = Path.exists(deployment_file_abs_path)

print(f"Deployment file {deployment_file} exists: {deployment_exists}")
print(f"Deployment file abs path: {deployment_file_abs_path}")

deployment_file_is_file = deployment_file_abs_path.is_file()
deployment_file_is_directory = deployment_file_abs_path.is_dir()

print(f"Deployment file is file: {deployment_file_is_file}")
print(f"Deployment file is directory: {deployment_file_is_directory}")

extension = deployment_file_abs_path.suffix

print(f"Deployment file extension: {extension}")

deployment_file_contents = deployment_file_abs_path.read_text()

print(f"Deployment file contents: {deployment_file_contents}")

test_file_name = "test_file"

test_file_folder = "test_file_folder"

test_file_folder = script_folder / test_file_folder

if not test_file_folder.exists():
    print(f"The folder {test_file_folder} does not exist. Creating it ...")
    Path.mkdir(test_file_folder)
else:
    print(f"The folder {test_file_folder} exists. Skipping ...")

test_extensions = [".yaml", ".json", ".txt", ".log"]

for extension in test_extensions:
    new_file = test_file_name + extension
    print(f"New file: {new_file}")
    new_file_abs_path = script_folder / test_file_folder / new_file
    print(f"New file abs path: {new_file_abs_path}")
    now = datetime.now()
    iso_timestamp = now.isoformat()
    if not new_file_abs_path.exists():
        with open(new_file_abs_path, "w", encoding="utf-8") as f:
            f.write(f"File name: {new_file}\n")
            f.write(f"File created at: {iso_timestamp}\n")
    with open(new_file_abs_path, "a", encoding="utf-8") as f:
        f.write(f"Latest run: {iso_timestamp}\n")
