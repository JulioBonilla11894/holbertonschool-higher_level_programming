from os.path import exists

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

def generate_invitations(template, attendees):
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(template, str):
        print("template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("attendees must be a list of dictionaries")
        return

    for i in range(len(attendees)):
        template_schema = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeHolder = "{" + f"{key}" + "}"
            value = attendees[i].get(key) or "N/A"
            template_schema = template_schema.replace(placeHolder, value)

        if not exists(f"output_{i + 1}.txt"):
            with open(f"output_{i + 1}.txt", "w") as text_file:
                text_file.write(template_schema)
        else:
            print("Output file already exists")
