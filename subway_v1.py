# -*- coding: UTF-8 -*-

'''
ver 0.1
>나이/환승여부
>5번까지 환승가능

ver 1.0
>지하철간 환승안됨

ver 1.1
>같은 버스 환승안됨

ver 2.0
>카드찍는 기계 클래스 다르게 하기
>환승거리별 요금추가 달리
'''


#class 정의 : 사람 / 카드 / 역
class human():
	name = 0
	age = 0

	def brain(self):
		start_end = input ('환승하시겠습니까? (yes = 1, no = 2)')

class card():
	basic_price = 0
	transfer_price = 0
	transfer_num = 0
	money = 0

	def price(self): #나이에 따라 기본요금/환승요금 설정
		if user.age == 1:
			self.basic_price = 900
			self.transfer_price = 50
		else:
			self.basic_price = 1000
			self.transfer_price = 100

	def transfer_count(self): #환승카운트 올리기
		if 0 <= self.transfer_num < 4:
			self.transfer_num = self.transfer_num + 1
		else: # 4초과시 0으로 초기화
			self.transfer_num = 0
			print "환승 횟수가 초과되어, 다음번엔 환승이 적용 되지 않습니다."

class station():

	payment = 0

	def check_payment(self):
		if 0 < Tmoney.transfer_num <= 4: #환승일 경우 기본비용 0만들기
			self.payment = Tmoney.basic_price*0 + Tmoney.transfer_price
		else: #환승이 아닐경우 환승비용을 0으로 만들기
			self.payment = Tmoney.basic_price + Tmoney.transfer_price*0

		Tmoney.money = Tmoney.money - self.payment #잔액만들기

	def door(self):
		if Tmoney.money < Tmoney.basic_price:
			print '요금이 부족합니다 error ---'
			Tmoney.money = input('얼마를 충전하시겠습니까? : ')

		else:
			print "\n\n-----%s의 카드정보-----" % user.name
			print "비용 : ", self.payment
			print "잔액 : " , Tmoney.money
			print "남은 환승횟수 : ", 4-Tmoney.transfer_num
			print "-----------------------\n\n"


#사람정의 / 카드 구입 / 지하철역 선정
user = human()
Tmoney = card()
konkuk = station()
start_end = 1 # 환승 확인

'''
#test
user.name = 'A'
user.age = 2
Tmoney.money = 50000
Tmoney.price() # 카드 정보체크
'''


#user 정보 정리 / 카드 충전
user.name = raw_input("what is your name? : ")
user.age = input("당신의 연령은? (청소년=1, 성인 = 2) : ")
Tmoney.money = input('얼마를 충전하시겠습니까? : ')
Tmoney.price() # 카드 정보체크


#탑승시작
print ("-----------탑승시작------------\n")

while start_end==1:
	start_end = 0
	konkuk.check_payment()
	konkuk.door()
	Tmoney.transfer_count()
	print Tmoney.transfer_num
	start_end = start_end = input ('환승하시겠습니까? (yes = 1, no = 2)')

print '\n\n\n이용해주셔서 감사합니다.'


'''
수정사항
1. 처음 카드를 찍을때 돈이 없을 경우
	>문이 안열려야 함.
	>환승카운트가 안되어야 함
'''