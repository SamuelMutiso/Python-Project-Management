# storage.py - handles reading and writing JSON data files
# all data is saved in the data/ folder

import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")


def setup_data_folder():
    
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    for filepath in [USERS_FILE, PROJECTS_FILE, TASKS_FILE]:
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)


def load_data(filepath):
    
    setup_data_folder()
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(filepath, data):
    
    setup_data_folder()
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)