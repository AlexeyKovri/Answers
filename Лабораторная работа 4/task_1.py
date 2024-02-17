# TODO решите задачу
import json

INPUT_FILE = "input.json"


def task() -> float:
    result = 0
    with open(INPUT_FILE, "r") as file:
        json_data = json.load(file)
        for item in json_data:
            result += item["score"] * item["weight"]
    return round(result, 3)


print(task())
