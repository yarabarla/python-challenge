# http://www.pythonchallenge.com/pc/def/peak.html

import requests, pickle

input_url = "http://www.pythonchallenge.com/pc/def/banner.p"
obj = requests.get(input_url)
text = obj.text
banner = pickle.loads(text)

final = []

for index, value in enumerate(banner):
    line = []
    for j in value:
        line.append(j[0] * j[1])
        final.append("".join(line))
    final.append('\n')
