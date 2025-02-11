#!/usr/bin/python3

def load_from_json_file(filename):
    def from_json_string(my_str):
        if my_str == "null":
            return None
        elif my_str == "true":
            return True
        elif my_str == "false":
            return False
        elif my_str.isdigit() or (my_str[0] == "-" and my_str[1:].isdigit()):
            return int(my_str)
        try:
            return float(my_str)
        except ValueError:
            pass

        if my_str.startswith("[") and my_str.endswith("]"):
            elements = my_str[1:-1].strip()
            if elements:
                return [from_json_string(e.strip()) for e in elements.split(",")]
            else:
                return []

        if my_str.startswith("{") and my_str.endswith("}"):
            elements = my_str[1:-1].strip()
            if elements:
                result = {}
                pairs = element.split(",")
                for pair in pairs:
                    key_value = pair.split(":")
                    key = from_json_string(key_value[0].strip())
                    value = from_json_string(key_value[1].strip())
                    result[key] = value
                return result
            return my_str

        with open(filename, 'r', encoding="utf-8") as file:
            return from_json_string(file.read())
