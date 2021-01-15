import json
from pathlib import Path

def load_config_json(json_path: Path):
    return json.load(json_path)