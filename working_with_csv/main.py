import sys
import json
import requests
import tempfile
import csv

url = "https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json"

with tempfile.TemporaryDirectory() as tmpdirname:  # создаём временную директорию; она существует, пока мы в блоке with
    # сохраняем файл в этой директории а вот эта строка должна будет конфликтовать с предыдущим коммитом
    # url_data = requests.get(sys.argv[1])
    url_data = requests.get(url)
    with open(tmpdirname + '/local.json', 'wb') as file:
        file.write(url_data.content)
    # #открываем файл и работаем с ним
    f = open(tmpdirname + '/local.json', 'r')
    json_data = json.load(f)
    f.close()
    attributes = json_data[0].keys()
    with open('local.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(json_data[0].keys())
        for object in json_data:
            writer.writerow([object[attribute] for attribute in attributes])
    f.close()