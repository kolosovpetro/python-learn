from pathlib import Path

import yaml

yaml_file_name = "config.yaml"

script_directory = Path(__file__).resolve().parent

print(f"YAML file name: {yaml_file_name}")
print(f"Script abs path: {script_directory}")

yaml_file_abs_path = script_directory / yaml_file_name

print(f"YAML file abs path: {yaml_file_abs_path}")

data = {
    "animals": ["cat", "dog", "frog"],
    "application": {
        "environment": "production",
        "users": ["alex", "bob", "clara"],
        "id": [1, 2, 3, 4, 5],
    },
    "year": 2026,
    "person": {
        "name": "Devon",
        "surname": "Larrat",
        "age": 51,
    },
}

with open(yaml_file_abs_path, "w", encoding="utf-8") as file:
    yaml.safe_dump(
        data,
        file,
        sort_keys=False,
        default_flow_style=False,
    )

print(f"File is created {yaml_file_name}")
