# Converter "Standalone"

import json
from tkinter import filedialog


def read_data():
    file_path = filedialog.askopenfilename(
    title="Open JSON file", filetypes=[("JSON files", "*.json")], defaultextension=".json"
)
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)
        return {}


def switch_key_value(data):
    new_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            new_data[value] = key
        else:
            print(f"Skipping key '{key}': value is not a string")
    print("Preview:")
    for i, (k, v) in enumerate(new_data.items()):
        print(f"{k} : {v}")
        if i >= 5:
            print("...")
            break
    return new_data


def write_data_json(data):
    file_path = filedialog.asksaveasfilename(title="save file",defaultextension="*.json")
    try:
        with open(file_path,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)
            print("data save")
    except Exception as e:
        print(e)


def final_pipeline():
    data = read_data()
    data_to_write = switch_key_value(data)
    write_data_json(data_to_write)


final_pipeline()



