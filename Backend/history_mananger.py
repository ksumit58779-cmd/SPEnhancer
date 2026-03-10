# history_mananger.py
import json
import os
from datetime import datetime

# ── Build absolute path so it always works ──
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DATA_DIR     = os.path.join(BASE_DIR, "..", "data")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")


def _load():
    # If file doesn't exist yet, return empty list
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def _save(data):
    # Always create the data/ folder if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_history(original: str, enhanced: str, mode: str):
    history = _load()
    entry = {
        "id":        len(history) + 1,
        "original":  original,
        "enhanced":  enhanced,
        "mode":      mode,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    history.insert(0, entry)  # newest first
    _save(history)


def get_history():
    return _load()


def clear_history():
    _save([])