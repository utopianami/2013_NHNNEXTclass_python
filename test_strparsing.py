

test_str = '[Fri Oct 05 08:18:16 2012] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico'





def find_error(find_str):
	find = find_str.split('[:]')
	print find

	for word in find_str:
		if word == '[error]':
			print ' error '
		else:
			print '2'

find_error(test_str)