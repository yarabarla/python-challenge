# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests, re

nothing = 63579 # Initial nothing value, prompted to change during program
url =  "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"

while True:
    req = requests.get(url % nothing)
    data = req.text # Stores body of text to be parsed
    pattern = re.compile('\d+')

    try:
        nums = pattern.findall(data)
        nothing = int("".join(nums))
        print data #To read the prompts that occasionally show up

    except:
        break


print "Data is: %s and nothing is %d" % (data, nothing)


