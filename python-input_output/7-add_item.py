#!/usr/bin/python3

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    current_list = load_from_json_file(filename)
except FileNotFoundError:
    current_list = []

current_list.extend(sys.argv[1:])

save_to_json_file(current_list, filename)
