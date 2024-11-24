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
        import csv
import json

import csv
import json

def jsontocsv(json_filename, csv_filename):
    """
    Переписує дані з .json у .csv файл, додаючи нові рядки.
    """
    try:
        # Відкриваємо .json файл для читання
        with open(json_filename, 'r') as jsonfile:
            data = json.load(jsonfile)  # Завантажуємо дані з JSON
        
        # Нові рядки для додавання
        new_data = [
            {'name': 'Yaroslav', 'age': '18', 'city': 'Konotop'},
        ]
        
        # Додаємо нові рядки до існуючих даних
        data.extend(new_data)
        
        # Отримуємо список заголовків (ключів з першого словника)
        fieldnames = data[0].keys()

        # Створюємо .csv файл і записуємо дані
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Записуємо заголовки
            writer.writerows(data)  # Записуємо всі рядки

        print(f"Дані успішно переписані у {csv_filename}. Нові рядки додано.")

    except FileNotFoundError:
        print(f"Помилка: файл {json_filename} не знайдено.")
    except json.JSONDecodeError:
        print("Помилка: Невірний формат .json файлу.")
    except Exception as e:
        print(f"Несподівана помилка: {str(e)}")

# Основний блок виконання програми
if __name__ == "__main__":
    # Ім'я .json файлу, створеного першим студентом
    input_json = 'people.json'
    
    # Ім'я нового .csv файлу
    output_csv = 'updated_people.csv'

    # Виконуємо конвертацію
    try:
        jsontocsv(input_json, output_csv)
        print("Data successfully written to updated_people.csv")
    except Exception as e:
        print(f"Error: {str(e)}")

