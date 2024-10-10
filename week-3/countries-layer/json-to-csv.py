import csv
import json

json_file_path = './json-countries-data/dki-jakarta-countries.json'
csv_file_path = './csv-countries-data/dki-jakarta-countries.csv'

# Read JSON data
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Open CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Code', 'Name', 'Latitude', 'Longitude', 'Google Place ID'])
    
    for entry in json_data['data']:
        writer.writerow([entry['code'], entry['name'], entry['coordinates']['lat'], entry['coordinates']['lng'], entry['google_place_id']])

print(f'Successfully create csv file: {csv_file_path}')
