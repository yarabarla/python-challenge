import re

file_ob = open("3.dat", 'r')
ob_read = file_ob.read()
read_arr = list(ob_read)

word = []

def for_loop(): # Loops through array to find solution
	for i in range(len(read_arr)):

		if (i + 8) > len(read_arr): # To keep index in bounds
			break

		if not(read_arr[i]).isupper() and (read_arr[i + 1]).isupper() and (read_arr[i + 2]).isupper() and (read_arr[i + 3]).isupper() and(read_arr[i + 4]).islower() and (read_arr[i + 5]).isupper() and (read_arr[i + 6]).isupper() and (read_arr[i + 7]).isupper() and not(read_arr[i + 8]).isupper(): 
		
			word.append(read_arr[i + 4])

	print "".join(word)


def reg_ex(): # Uses regex to find the pattern
	print "".join( re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", ob_read))


# for_loop()
# reg_ex() 
