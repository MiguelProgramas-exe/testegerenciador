# storage.py
import json
import os

PASTA_DATA = "data"

def _ensure_data_folder():
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA, exist_ok=True)

def _path(name):
    _ensure_data_folder()
    return os.path.join(PASTA_DATA, f"{name}.json")

def load(name):
    path = _path(name)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except json.JSONDecodeError:
            return []
    return []

def save(name, lst):
    path = _path(name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(lst, f, ensure_ascii=False, indent=4)