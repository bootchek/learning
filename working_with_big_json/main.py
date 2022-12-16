import sys
import json
import requests
import tempfile

# f = open(sys.argv[1])
url = 'https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json'
temp = tempfile.NamedTemporaryFile()
# data = json.loads(requests.get(url).text) # вот в этой переменной хранятся объекты json'а;
# я бы так работал (поместил в переменную питона данные из внешнего json'а_, если бы не знал про временные файлы

# Выдаёт все данные из json'а в виде строки
with tempfile.TemporaryFile() as tmp:
    tmp.write(bytes(requests.get(url).text, 'utf-8'))
    tmp.seek(0)
    data = json.loads(tmp.read())

print(data[0])
# f = tempfile.TemporaryFile(mode='w+t')
# try:
#     f.writelines(['first\n', 'second\n'])
#     f.seek(0)
#
#     for line in f:
#         print line.rstrip()
# finally:
#     f.close()




# k, n, i = sys.argv[2], 0, 0
# data = json.load(f)
# while i < len(data):
#     json_list = []
#     for i in range(i, i + int(k)):
#         if i == len(data):
#             break
#         else:
#             json_list.append(data[i])
#     n += 1
#     i += 1
#     with open(sys.argv[3]+"file_" + str(n) + ".json", "w") as outfile:
#         json.dump(json_list, outfile, indent=2)
