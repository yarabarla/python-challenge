# http://www.pythonchallenge.com/pc/def/peak.html

import requests, pickle

input_url = "http://www.pythonchallenge.com/pc/def/banner.p"
obj = requests.get(input_url)
text = obj.text

banner = pickle.loads(text)
print banner
