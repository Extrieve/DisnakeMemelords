import json
import csv


with open('themes3.json', 'r', encoding='utf-8') as f:
    themes_data = json.load(f)


registered_ids = []

for entry in themes_data:
    if entry['anime_id'] not in registered_ids:
        registered_ids.append(entry['anime_id'])


print(registered_ids)

# save registered id to csv
with open('registered_ids2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['anime_id'])
    for id in registered_ids:
        writer.writerow([id])
