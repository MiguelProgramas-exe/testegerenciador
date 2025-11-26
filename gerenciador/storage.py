import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

FILES = {
    "usuarios": DATA_DIR / "usuarios.json",
    "projetos": DATA_DIR / "projetos.json",
    "tarefas": DATA_DIR / "tarefas.json",
}

def read_json(key):
    path = FILES[key]
    if not path.exists():
        path.write_text("[]", encoding="utf-8")
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_json(key, data):
    path = FILES[key]
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
