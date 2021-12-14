import json
from types import SimpleNamespace

def load_config_json(json_path: str):
    return json.load(open(json_path), object_hook=lambda d: SimpleNamespace(**d))