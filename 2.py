import sys

file_ob = open("2.dat", 'r')
file_read = file_ob.read()

file_list = list(file_read)


for i in range(len(file_list)):
	if (file_list[i]).isalpha():
		sys.stdout.write(file_list[i])

print '\n'
