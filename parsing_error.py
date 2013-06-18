# -*- coding: UTF-8 -*-

'''
-flow
	1. read_file
	2. def make_log
		2.1 make_dic
		2.2 sort
		2.3 print (Summary + Detail)
		
	3. run
'''

#1. read_file : 각 라인을 리스트로 저장
origin_file = open('error_log')
Lines_file = origin_file.readlines()

#2. def make_log
def make_log(origin):
	#2.1 make_dic
	dic_errorlog = {}

	for Oneline in origin:

		#2.2 check_error
		if Oneline.find('error') != -1 :

			#parsing_2ed[0] = sort / parsing_2ed[1] = address
			parsing_1st = Oneline.split('] ')
			parsing_2ed = parsing_1st[3].split(': /')


			if parsing_2ed[0] not in dic_errorlog:
				dic_errorlog[parsing_2ed[0]] = {'list' : [] , 'count' : 0}
			else:
				dic_errorlog[parsing_2ed[0]]['list'].append(parsing_2ed[1])
				dic_errorlog[parsing_2ed[0]]['count'] += 1


	#2.3 print
	print '[Summary]'
	for keys in dic_errorlog:
		print keys, dic_errorlog[keys]['count']

	print '[Detail]'
	print '-----------------'
	for keys in dic_errorlog:
		print keys
		for each in dic_errorlog[keys]['list']:
			print each


#3. run
make_log(Lines_file)






