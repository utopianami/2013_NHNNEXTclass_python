
numberList = []

def makeList(list):
	for rows in range(1,10):
		list.append([])
		for cols in range(1, 10):
			list[rows-1].append(rows*cols)

makeList(numberList)

for row in range(0, 9):
	print numberList[row]