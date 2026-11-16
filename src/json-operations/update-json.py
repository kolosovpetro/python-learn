import json
from pathlib import Path

script_folder = Path(__file__).resolve().parent

file_name = "write.json"

file_abs_path = script_folder / file_name

print(f"File abs path: {file_abs_path}")

with open(file_abs_path, encoding="utf-8") as file:
    data = json.load(file)

print(
    "Json file has been loaded successfully",
    f"File path: {file_abs_path}",
    f"File data: {data}",
)

print(f"Username: {data['user']['name']}")
print(f"Age: {data['user']['age']}")

print("Updating json data...")

data["user"]["name"] = "John"
data["user"]["surname"] = "Brzenk"

print(
    "Updated data:",
    f"{data}",
)

with open(file_abs_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print("The file has been updated successfully.")
