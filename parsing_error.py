
#1 read_file
origin_file = open('error_log', 'r')
readLine = origin_file.readlines() 



#2 count_error
def count_error(text):
	error_num = 0
	warn_num = 0 
	notice_num = 0

	for line in text:
		if line.find('[error]') != -1 :
			error_num = error_num + 1
		elif line.find('[warn]') != -1 :
			warn_num = warn_num + 1
		elif line.find('[notice]') != -1 :
			notice_num = notice_num + 1

	print error_num
	print warn_num
	print notice_num

#
count_error(readLine)



#code_error
try : 
	origin_file2 = open('error_log')
	readLine = origin_file2.readlines() 

except IOError:
	print "input& output!!\nOMG!!!!!!"

except:
	print "OMG!!!!"

finally :
	print "Yo~Man~\ngood man~"