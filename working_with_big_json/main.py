import sys
import json
import requests
import tempfile

# https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json

with tempfile.TemporaryDirectory() as tmpdirname: #создаём временную директорию; она существует, пока мы в блоке with
    # сохраняем файл в этой директории
    url_data = requests.get(sys.argv[1])
    with open(tmpdirname+'/local.json', 'wb') as file:
        file.write(url_data.content)
    #открываем файл и работаем с ним
    f = open(tmpdirname+'/local.json', 'r')
    json_data = json.load(f)
    k, n, i = sys.argv[2], 0, 0
    while i < len(json_data):
        json_list = []
        for i in range(i, i + int(k)):
            if i == len(json_data):
                break
            else:
                json_list.append(json_data[i])
        n += 1
        i += 1
        with open(sys.argv[3]+"file_" + str(n) + ".json", "w") as outfile:
            json.dump(json_list, outfile, indent=2)
