# -*- coding : utf-8 -*-


#1 read_file
file = open('error_log', 'r')
readLine = file.readlines() 


#2 num_error

error_num = 0
def count_error(text):
	text = text.split('[:]')
	for word in text:
		if word == [error]:
			error_num = error_num + 1
		else:
			pass

count_error(readLine)


print error_num