import json

with open("data.json", "r", encoding="utf8") as f:
    text=json.load(f)

i = 0
for i in range(10):
    for j in text[i]: 
        print(j)
        i += 1