import sys, re

file_ob = open("2.dat", 'r')
file_read = file_ob.read()

file_list = list(file_read)

def for_loop():

	for i in range(len(file_list)):
		if (file_list[i]).isalpha():
			sys.stdout.write(file_list[i]) # Needed so all the letters print on the same line.

	print '\n'


def reg_ex():

	pattern = re.compile("[a-z]", re.I) # I stands for IGNORECASE
	print "".join(pattern.findall(file_read))


# for_loop()
# reg_ex()
