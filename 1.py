import string

solve = "pythonchallenge.com/pc/def/map.html" 

def shift_cypher(value, orig):

	finish = ""

	for i in orig:
		if i.isalpha(): # cypher only works with letters
			if ord(i) + value > 122: # 122 is the value for 'z'. For looping value back to 'a'
				i = chr(97 + (ord(i) + value - 122) - 1) # 97 is 'a', -1 to add value properly	
		
			else:
				i = chr(ord(i) + value)

		finish += i

	return finish

# String Translate Method:

shift = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print solve.translate(shift)

# Shift Cypher Method:

print shift_cypher(2, solve)
