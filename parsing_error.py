# -*- coding: UTF-8 -*-

'''
-flow
	1. read_file
	2. def make_log
		2.1 count_error
		2.2 make_dic
		2.3 sort
		2.4 print (Summary + Detail)
		
	3. run
'''

#1. read_file : 각 라인을 리스트로 저장
origin_file = open('error_log')
Lines_file = origin_file.readlines()

#2. def make_log
def make_log(origin):
	#count error
	num_File = 0
	num_Invalid = 0
	num_script = 0
	num_client = 0
	num_attempt = 0
	total_error = num_File+num_Invalid+num_script+num_client+num_attempt

	#make_dic
	dic_errorlog = {'File does not exist' : [] ,
	'Invalid URI in request GET invalid' : [],
	'script not found or unable to stat' : [],
	'client denied by server configuration' : [], 
	'attempt to invoke directory as script' : []}

	for Oneline in origin:

		#check_error
		if Oneline.find('error') != -1 :

			#parsing : parsing[0]=sort, parsing[1]=addres
			parsing = Oneline.split(': /')

			#sort_error + append_dic
			if parsing[0].find('File') != -1 :
				num_File += 1
				dic_errorlog['File does not exist'].append(parsing[1])

			elif parsing[0].find('Invalid') != -1 :
				num_Invalid += 1
				dic_errorlog['Invalid URI in request GET invalid'].append(parsing[1])

			elif parsing[0].find('script') != -1 :
				num_script += 1
				dic_errorlog['script not found or unable to stat'].append(parsing[1])

			elif parsing[0].find('client') != -1 :
				num_client += 1
				dic_errorlog['client denied by server configuration'].append(parsing[1])

			elif parsing[0].find('attempt') != -1 :
				num_attempt += 1
				dic_errorlog['ttempt to invoke directory as script'].append(parsing[1])

	#print [Summary]
	print '[Summary]\n'
	print 'TOTAL error : ', total_error
	print '\nFile does not exist : ', num_File
	print '\nInvalid URI in request GET invalid : ',num_Invalid
	print '\nscript not found or unable to stat : ', num_script
	print '\nclient denied by server configuration : ', num_client
	print '\nattempt to invoke directory as script : ', num_attempt

	
	#print [Detail]
	print '\n[Detail]'
	print '------------------------'
	print '1. File does not exist'
	for each in dic_errorlog['File does not exist']:
		print each
	print '\nInvalid URI in request GET invalid : ',num_Invalid
	for each in dic_errorlog['Invalid URI in request GET invalid']:
		print each
	print '\nscript not found or unable to stat : ', num_script
	for each in dic_errorlog['script not found or unable to stat']:
		print each
	print '\nclient denied by server configuration : ', num_client
	for each in dic_errorlog['client denied by server configuration']:
		print each
	print '\nattempt to invoke directory as script : ', num_attempt
	for each in dic_errorlog['attempt to invoke directory as script']:
		print each

#3. run
make_log(Lines_file)