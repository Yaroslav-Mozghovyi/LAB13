import csv
import json

def createcsv(filename, data):
    """Створює .csv файл та записує в нього дані."""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def csvtojson(csv_filename, json_filename):
    """Переписує дані з .csv у .json файл."""
    data = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    with open(json_filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def jsontocsv(json_filename, csv_filename):
    """Переписує дані з .json в .csv, додаючи нові рядки."""
    try:
        with open(json_filename, 'r') as jsonfile:
            data = json.load(jsonfile)
        
        new_data = [
            {'name': 'Denys', 'age': '18', 'city': 'Sumy'},
            {'name': 'Diana', 'age': '18', 'city': 'Sumy'}
        ]
        
        data.extend(new_data)
        
        createcsv(csv_filename, data)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    data = [
        {'name': 'Yevhen', 'age': 18, 'city': 'Sumy'}
    ]
    
    try:
        createcsv('people.csv', data)
        csvtojson('people.csv', 'people.json')
    except Exception as e:
        print(f"Error: {str(e)}")
    
    try:
        jsontocsv('people.json', 'updated_people.csv')
        print("Data successfully written to updated_people.csv")
    except Exception as e:
        print(f"Error: {str(e)}")
