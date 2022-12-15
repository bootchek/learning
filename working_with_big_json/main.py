import sys
import json

f = open(sys.argv[1])
k, n, i = sys.argv[2], 0, 0
data = json.load(f)
while i < len(data):
    json_list = []
    for i in range(i, i + int(k)):
        if i == len(data):
            break
        else:
            json_list.append(data[i])
    n += 1
    i += 1
    with open(sys.argv[3]+"file_" + str(n) + ".json", "w") as outfile:
        json.dump(json_list, outfile, indent=2)
