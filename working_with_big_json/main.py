import sys
import json
import requests
import tempfile

# https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json

with tempfile.TemporaryDirectory() as tmpdirname: #создаём временную директорию; она существует, пока мы в блоке with
    # сохраняем файл в этой директорииbpvtyfsksdf
    url_data = requests.get(sys.argv[1])
    with open(tmpdirname+'/local.json', 'wb') as file:
        file.write(url_data.content)
    #открываем файл и работаем с ним
    f = open(tmpdirname+'/local.json', 'r')
    json_data = json.load(f)
    number_of_objects, number_of_files, i = sys.argv[2], 0, 0
    while i < len(json_data):
        json_list = []
        for i in range(i, i + int(number_of_objects)):
            if i == len(json_data):
                break
            else:
                json_list.append(json_data[i])
        number_of_files += 1
        i += 1
        with open(sys.argv[3]+"file_" + str(number_of_files) + ".json", "w") as outfile:
            json.dump(json_list, outfile, indent=2)
