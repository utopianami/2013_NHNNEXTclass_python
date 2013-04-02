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
	decision = 0

	def brain(self):
		self.decision = input ('탑승(환승) 하시겠습니까? (yes = 1, no = 2)')
	
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
		if self.transfer_num <0: #처음에 돈이 없어서 문이 열리지 않을때
			self.transfer_num = 0
		elif 0 <= self.transfer_num < 4: #환승할때
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

	def door(self):
		if  self.payment <= Tmoney.money:
			print "\n\n-----%s의 카드정보-----" % user.name
			print "비용 : ", self.payment
			Tmoney.money = Tmoney.money - self.payment#잔액만들기
			print "잔액 : " , Tmoney.money
			print "남은 환승횟수 : ", 4-Tmoney.transfer_num
			print "-----------------------\n\n"

		else:
			print '요금이 부족합니다. error ---'
			print '현재 잔액 : ', Tmoney.money
			print '필요 금액', self.payment, '\n\n'
			Tmoney.money = input('얼마를 충전하시겠습니까? : ')
			Tmoney.transfer_num = Tmoney.transfer_num -1 #환승카운트 올리지 않기
			


#사람정의 / 카드 구입 / 지하철역 선정 /
user = human()
Tmoney = card()
konkuk = station()

#user 정보 정리 / 카드 충전
user.name = raw_input("what is your name? : ")
user.age = input("당신의 연령은? (청소년=1, 성인 = 2) : ")
Tmoney.money = input('얼마를 충전하시겠습니까? : ')
Tmoney.price() # 카드 정보체크


#탑승시작
print ("-----------탑승시작------------\n")

while 1: 
	konkuk.check_payment() #요금확인 (환승일 경우 & 미환승일 경우)
	konkuk.door() #기계 프린트()
	Tmoney.transfer_count() #환승횟수 설정
	user.brain()

	if user.decision == 2:
		break

print '\n\n\n이용해주셔서 감사합니다.'