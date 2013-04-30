
#1 read_file
origin_file = open('error_log', 'r')
readLine = origin_file.readlines() 



#2 count_error
def count_error(text):
	error_num = 0
	for line in text:
		if line.find('[error]') != -1 :
			error_num = error_num + 1

	print error_num


#
count_error(readLine)
