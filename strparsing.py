

test_str = '[Fri Oct 05 08:18:16 2012] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico'





def find_error(find_str):
	find_str = test_str.split('[:]')
	print find_str
'''
	for i in find_str:
		if i == '[error]':
			print ' error '
		else:
			print '2'
'''
find_error(test_str)