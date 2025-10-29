import json

json_in_string ='{"Information": {"SchoolDetails": [{"Name": "VidhyaMandhir"}, {"Name": "Chettinad"}, {"Name":"PSSenior"}]}}'
json_word = json.loads(json_in_string)
json_word['test'] = True
new_json = json.dumps(json_word,indent=2)
print(json_word["Information"]["SchoolDetails"][0])
print(new_json)
print(json_word["test"])
print(json_in_string)

with open("example.json", "r") as ex :
    data = json.load(ex)

with open("ex2.json", "w") as e2 :
    json.dump(data, e2, indent=2)

print(data["id"])