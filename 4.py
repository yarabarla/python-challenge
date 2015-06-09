# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests, re

nothing = 12345 # Initial nothing value
url =  "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"

req = requests.get(url % nothing) 
data = req.text # Stores body of text to be parsed

pattern = re.compile('\d+')
nums = pattern.findall(data)
nothing = int("".join(nums))
print nothing
