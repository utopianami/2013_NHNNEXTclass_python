# -*- coding: UTF-8 -*-
import math

#homework_3_youngnamlee_131052



#exrcise1
print 'exrcise1'

def print_rename(first_name,last_name):
	print 'Your name : \n', first_name
	print 'he is from' , last_name ,'family'

print_rename("youngnam","lee")




#exrcise2
print '\n\n\nexrcise2'
def absolute_Value(num):
	if num >= 0:
		print num
	else:
		print -(num)

input_num = input('input your number : ')
absolute_Value(input_num)


#exrcise3
print '\n\n\nexrcise3'

def change_Value(num):
	if  0< num <= 10:
		print num+10
	elif 10 < num < 100:
		print num*0.1
	else:
		print False

input_num2 = input('input your number : ')
change_Value(input_num2)



#exrcise4
print '\n\n\nexrcise4'

def distance_Value(x1, y1, x2, y2):
	before = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
	distance = math.sqrt(before)
	print distance


input_Pvalue = input('input P value(ex : 3 4) :')
input_Qvalue = input('input Q value(ex : 5 8) :')

distance_Value(input_Pvalue[0], input_Pvalue[1], input_Qvalue[0], input_Qvalue[1])

#exrcise5
print '\n\n\nexrcise5'

count = 0
for char in 'next people':
	if char == 'e':
		count = count + 1
	else:
		count

print count


#exrcise6
print '\n\n\nexrcise6'

word = raw_input("input your word : ")
length = len(word) #글자 길이 체크
count = 0 #같은 글자 체크


for i in range(length):
	reverse = length - i - 1 #숫자를 반대로 넣기
	if word[i] == word[reverse]:
		count = count + 1
	else:
		count

if count == length:
	print 'same'
else:
	print 'different'
