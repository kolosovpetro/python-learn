import json
from pathlib import Path

fruits = ["apple", "orange", "banana"]

message = "Hello, Python!"

age = 24

file_name = "write.json"

print(f"File name: {file_name}")

script_location = Path(__file__).resolve().parent

file_abs_path = script_location / file_name

print(f"File ABS path: {file_abs_path}")

data = {
    "fruits": fruits,
    "message": message,
    "age": age,
    "nested_obj": {
        "array": fruits,
        "integers": [1, 2, 3, 4, 5],
    },
    "user": {
        "name": "Petro",
        "surname": "Kolosov",
        "age": "22",
    },
}

print(f"Data: {data}")

with open(file_abs_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print("File has been created successfully.")
