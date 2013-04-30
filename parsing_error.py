
#1 read_file
origin_file = open('error_log', 'r')
readLine = origin_file.readlines() 



#2 count_error
def count_error(text):
	index = 0
	error_num = 0
	warn_num = 0 
	notice_num = 0
	erorr_list = []

	#count_erorr_num
	for line in text:
		if line.find('[error]') != -1 :
			error_num = error_num + 1
			erorr_list.append(index)
		elif line.find('[warn]') != -1 :
			warn_num = warn_num + 1
		elif line.find('[notice]') != -1 :
			notice_num = notice_num + 1
		index = index + 1

	print '[SUMMARY REPORT]'
	print 'error : ', error_num
	print 'warn : ', warn_num
	print 'notice : ', notice_num

	#summary report_error

	file_num = 0
	Invalid_num = 0
	script_num = 0


	for message in text[index]:
		for word in message:
			if word == 'file':
				file_num += 1 
			elif word == Invalid:
				Invalid_num += 1
			elif word == script:



	print '[SUMMARY REPORT_eroor]'
	print "File does not exist : "
	print "Invalid URI in request GET invalid : "
	print "script not found or unable to stat : "
	print "client denied by server configuration : "
	print "attempt to invoke directory as script : " 



	print '-----erorr_list-----'
	for i in erorr_list:
		print readLine[i]
	print '-------------------'


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