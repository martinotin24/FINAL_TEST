#!/usr/bin/env python3
import cgi
import html

print("Content-Type: text/html\n")

party_items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service",
    "DJ", "Photo Booth", "Tables", "Chairs", "Drinks",
    "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
]
item_values = [20, 21, 10, 5, 8, 3, 15, 7, 12, 6, 9, 18, 4, 2, 11]

form = cgi.FieldStorage()
indices = form.getlist("items")

try:
    selected_indices = [int(i) for i in indices]
except ValueError:
    selected_indices = []

html_output = "<html><head><title>Digital Party Planner</title></head><body>"
html_output += "<h1>Digital Party Planner Results</h1>"

if not selected_indices:
    html_output += "<p>No items selected.</p>"
else:
    selected_items = [party_items[i] for i in selected_indices if 0 <= i < len(party_items)]
    selected_values = [item_values[i] for i in selected_indices if 0 <= i < len(item_values)]

    base_code = selected_values[0]
    expression = str(selected_values[0])
    for val in selected_values[1:]:
        base_code = base_code & val
        expression += f" & {val}"

    if base_code == 0:
        final_code = base_code + 5
        message = "Epic Party Incoming!"
        operation = f"{base_code} + 5 = {final_code}"
    elif base_code > 5:
        final_code = base_code - 2
        message = "Let's keep it classy!"
        operation = f"{base_code} - 2 = {final_code}"
    else:
        final_code = base_code
        message = "Chill vibes only!"
        operation = f"{base_code} (no change)"

    html_output += f"<p><strong>Selected Items:</strong> {', '.join(selected_items)}</p>"
    html_output += f"<p><strong>Base Party Code:</strong> {expression} = {base_code}</p>"
    html_output += f"<p><strong>Adjusted Party Code:</strong> {operation}</p>"
    html_output += f"<p><strong>Final Party Code:</strong> {final_code}</p>"
    html_output += f"<p><strong>Message:</strong> {message}</p>"

html_output += "</body></html>"
print(html_output)
