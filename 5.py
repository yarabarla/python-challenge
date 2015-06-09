# http://www.pythonchallenge.com/pc/def/peak.html

import requests

input_url = "http://www.pythonchallenge.com/pc/def/banner.p"
obj = requests.get(input_url)
banner = obj.text

print banner

