import os
import json
import pandas as pd


def save_response_to_file(data: dict, filename: str = "response.json"):
    filepath = os.path.join("data", filename)
    os.makedirs("data", exist_ok=True)

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.append(data)

    with open(filepath, "w") as f:
        json.dump(existing_data, f, indent=4)

    return f"{filename} updated successfully with new entry in {filepath}"


def load_responses_from_file(filename: str = "response.json"):
    filepath = os.path.join("data", filename)

    try:
        if not os.path.exists(filepath):
            print(f"{filename} not found")
            return []
        else:
            with open(filepath,"r") as f:
                loaded_json = json.load(f)
                return loaded_json

    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []



def filter_by_name(name: str , data: list):
        matches = []
        for record in data:
            if record.get("name", "").lower() == name.lower():
                matches.append(record)
        return matches

def average_age(data: list):
        ages = [record["age"] for record in data if isinstance(record.get("age"),(int,float))]

        if not ages:
            return 0.0

        return sum(ages)/len(ages)

def sort_by_age(data: list):
    valid_records = [record for record in data if isinstance(record.get("age"), (int, float))]
    sorted_records = sorted(valid_records, key=lambda x: x["age"], reverse=True)
    return sorted_records

def get_last_entries(data: list, count: int = 5):
    return data[-count:] if len(data) >= count else data


