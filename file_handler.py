"""
----------------------------------------------
File:         file_handler.py
Project:      To-Do List Manager
Description:  Handles loading and saving tasks.
Developed by: Huma Fatima
----------------------------------------------
"""
import json
import os

FILE_NAME = "tasks.json"

# Load Tasks

def load_tasks():

    if not os.path.exists(FILE_NAME):
        save_tasks([])
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        print("Warning: tasks.json is missing or corrupted.")
        print("Creating a new empty tasks file...")

        save_tasks([])
        return []

# Save Tasks

def save_tasks(tasks):
    
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(
            tasks,
            file,
            indent=4,
            ensure_ascii=False
        )