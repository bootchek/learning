import sys
import json
import requests
import tempfile
import csv

url = "https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json"


def first_function(url, outputfile_location):
    with tempfile.TemporaryDirectory() as tmpdirname:  # создаём временную директорию; она существует, пока мы в блоке with
        url_data = requests.get(sys.argv[1])
        # url_data = requests.get(url)
        with open(tmpdirname + '/local.json', 'wb') as file:  # сохраняем файл во временной директории
            file.write(url_data.content)
        f = open(tmpdirname + '/local.json', 'r')  # открываем файл и работаем с ним
        json_data = json.load(f)
        f.close()
        attributes = json_data[0].keys()  # получаем массив с названиями атрибутов каждого объекта из файла json
        with open(outputfile_location, 'w', newline='') as f:  # создаём csv-файл
            writer = csv.writer(f)
            writer.writerow(attributes)  # в первую строку записываем названия атрибутов
            for object in json_data:  # в следующие строки записываем значения атрибутов для каждого объекта
                writer.writerow(
                    [object[attribute] for attribute in attributes])  # вот тут я использую list comprehension
                # для прохождения по каждому атрибуту
        f.close()


first_function(url, "/Users/danilbuslaev/Desktop/local.csv")
