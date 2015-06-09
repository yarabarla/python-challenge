# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests, re

nothing = 12345 # Initial nothing value
url =  "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"

req = requests.get(url % nothing)
print req.text
