import csv
import json

csv_file = open("name_json.csv", encoding="latin-1")
csv_reader = csv.reader(csv_file)
reader_list = list(csv_reader)

data_list = []
for i in reader_list[1:]:
    data_list.append(i)

data_dict = {}

for i in range(len(data_list)):
    temp_dict = {"Nombre": "", "Id": "", "Email": "", "Edad": ""}
    keys_list = list(temp_dict.keys())
    for j in range(4):
        temp_dict[keys_list[j]] = data_list[i][j]
    data_dict["Persona" + str(i)] = temp_dict

json_string = json.dumps(data_dict)
json_loaded = json.loads(json_string)

for t in json_loaded:
    json_loaded[t]["Edad"] = len(json_loaded[t]["Email"])
    del(json_loaded[t]["Email"])

json_loaded_final = json.dumps(json_loaded)

with open("infoJson.txt", "w") as f:
    f.write(json_loaded_final)

with open("jSonFile.json", "w") as p:
    json.dump(json_loaded_final, p, indent=2)

print(json_loaded)
