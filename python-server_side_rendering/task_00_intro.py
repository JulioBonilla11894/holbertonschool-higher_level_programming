#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__} instead.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__} instead.")
        return

    # Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over attendees and create output files
    for index, attendee in enumerate(attendees):
        output = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A") or "N/A"
            output = output.replace(f"{{{placeholder}}}", value)

        output_filename = f"output_{index + 1}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output)
        print(f"Generated {output_filename}")

if __name__ == '__main__':
    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
