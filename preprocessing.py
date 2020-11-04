import json

file = open("Results.csv", "r+")

total_entries = 274

lines = []

for line in file:
    lines.append(line)

x = 0

changedline = []

for line in lines:
    line = line.replace("\"", "")

    if x != 0:
        line = "," + "\"" + str(x) + "\"" + ': ' + line[31:]
    else:
        line = "\"" + str(x) + "\"" + ': ' + line[31:]

    line = line[:-2]
    x += 1
    changedline.append(line)

filetxt = ''.join(changedline)

filetxt = '{"type":"MultiPolygon","coordinates": {' + filetxt + '}}'

print(filetxt)

with open('test_1.json', 'w') as json_file:
    json.dump(filetxt, json_file)
