from pathlib import Path

import yaml

yaml_file_name = "config.yaml"

script_directory = Path(__file__).resolve().parent

print(f"YAML file name: {yaml_file_name}")
print(f"Script abs path: {script_directory}")

yaml_file_abs_path = script_directory / yaml_file_name

print(f"YAML file abs path: {yaml_file_abs_path}")

with open(yaml_file_abs_path, encoding="utf-8") as file:
    data = yaml.safe_load(file)

animals = data["animals"]

data.pop("person", None)

print(
    f"Writing data to file {yaml_file_name}:",
    f"{data}",
)

with open(yaml_file_abs_path, "w", encoding="utf-8") as file:
    yaml.dump(
        data,
        file,
        sort_keys=False,
        default_flow_style=False,
    )

print("File updated successfully.")
