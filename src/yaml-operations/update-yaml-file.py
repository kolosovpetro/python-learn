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

print(
    "Received animals array:",
    f"{animals}",
)

data["animals"] = ["wolf", "fox", "lion"]

data["application"]["environment"] = "uat"


with open(yaml_file_abs_path, "w", encoding="utf-8") as file:
    yaml.safe_dump(
        data,
        file,
        sort_keys=False,
        default_flow_style=False,
    )

print(f"File is updated {yaml_file_name}")

print(
    "The new file data:",
    f"{data}",
)
