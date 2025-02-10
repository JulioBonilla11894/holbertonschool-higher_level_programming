#!/usr/bin/python3

def save_to_json_file(my_obj, filename):
    def to_json_string(my_obj):
        if isinstance(my_obj, dict):
            items = [f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()]
            return "{" + ", ".join(items) + "}"
        elif isinstance(my_obj, list):
            return "[" + ", ".join(to_json_string(item) for item in my_obj) + "]"
        elif isinstance(my_obj, bool):
            return "true" if my_obj else "false"
        elif my_obj is None:
            return "null"
        elif isinstance(my_obj, (int, float)):
            return str(my_obj)
        else:
            return f'"{my_obj}"'

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(to_json_string(my_obj))
