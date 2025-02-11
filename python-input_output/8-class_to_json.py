#!/usr/bin/python3

def class_to_json(obj):
    obj_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            obj_dict[key] = value

    return obj_dict
