import csv
import json

def createcsv(filename, data):
  with open(filename, 'w', newline='') as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

def csvtojson(csv_filename, json_filename):
  data = []
  with open(csv_filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      data.append(row)
  with open(json_filename, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
  data = [
    {'name': 'Yevhen', 'age': 18, 'city': 'Sumy'}
  ]
  try:
    createcsv('people.csv', data)
    csvtojson('people.csv', 'people.json')
  except Exception as e:
    print(f"Error: {str(e)}")