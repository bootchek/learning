import sys
import json
import requests
import tempfile
import csv
import time
from filesplit.split import Split
import os
import threading

url = "https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json"


def get_json_and_save_to_csv(url, outputfile_location):
    while True:
        with tempfile.TemporaryDirectory() as tmpdirname:  # создаём временную директорию; она существует, пока мы в блоке with
            # url_data = requests.get(sys.argv[1])
            url_data = requests.get(url)
            with open(tmpdirname + '/local.json', 'wb') as file:  # сохраняем файл во временной директории
                file.write(url_data.content)
            f = open(tmpdirname + '/local.json', 'r')  # открываем файл и работаем с ним
            json_data = json.load(f)
            f.close()
            attributes = json_data[0].keys()  # получаем массив с названиями атрибутов каждого объекта из файла json
            with open(outputfile_location + "local.csv", 'w', newline='') as csv_file:  # создаём csv-файл
                writer = csv.writer(csv_file)
                writer.writerow(attributes)  # в первую строку записываем названия атрибутов
                for object in json_data:  # в следующие строки записываем значения атрибутов для каждого объекта
                    writer.writerow(
                        [object[attribute] for attribute in attributes])  # вот тут я использую list comprehension
                    # для прохождения по каждому атрибуту
        print(f"The file has been downloaded and saved in csv format, path: {outputfile_location}local.csv")
        time.sleep(10)


def split_file_if_exists(path, number_of_pieces):
    while True:
        try:
            file_size = os.stat(path + 'local.csv').st_size
            split = Split(path + 'local.csv', path)
            split.bysize(size=round(file_size / number_of_pieces), newline=False, includeheader=False)
            os.remove(path + 'local.csv')
            print(f"The file has been splitted into {number_of_pieces} pieces and removed.")
            # return None
        except:
            print("The directory contains no such csv-file.")
        time.sleep(3)


first_function = threading.Thread(target=get_json_and_save_to_csv, args=(url, "/Users/danilbuslaev/Desktop/"))
second_function = threading.Thread(target=split_file_if_exists, args=("/Users/danilbuslaev/Desktop/", 4))
# get_json_and_save_to_csv(url, "/Users/danilbuslaev/Desktop/")
# split_file_if_exists("/Users/danilbuslaev/Desktop/", 4)
first_function.start()
second_function.start()