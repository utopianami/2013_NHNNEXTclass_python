# -*- coding: utf8 -*-


#사람 객체 생성
class person():
    #객체 생성과 동시에 나의 돈
    def __init__(self):
        self.my_money_dict = {5000 : 2 , 1000 : 1, 500 : 2 , 100 : 8}



class machine():
    #객체 생성과 동시에 생기는 리스트
    def __init__(self):
        self.products_dict = {
                    'vita500'   : {'price' : 500, 'number' : 2},
                    'milk'      : {'price' : 700, 'number' : 13},
                    'coffee'    : {'price' : 900, 'number' : 8}
                    }

        #잔액관리
        self.re_try = 0
        self.change = 0


    #돈 넣는 행위
    def get_inserted_money (self, person, my_money_dict) :

        #1: 돈을 투입합니다.
        self.inserted_money_sum = 0  #최종 투입된 금액

        while(True):
            print '\n내 주머니 상황'
            print '--------------------'
            for key,value in sorted(my_money_dict.items()):
                print "%d원이 %d개 있어요" % (key,value)

            self.inserted_money = raw_input('\n돈을 넣으세요(입금을 마치려면 0입력) : ')
            #입력 데이터를 숫자형으로 형변환 (왜냐면 $raw_input()은 숫자입력도 문자열로 입력을 받기때문)
            self.inserted_money = int(self.inserted_money)

            #엔터치면 돈 투입 끝으로 간주하고 while loop를 종료한다
            if self.inserted_money == 0:
                print '돈입력이 완료돠었습니다.'
                break

            #예외처리1 : 올바른 돈을 넣지 않은 경우(나의 딕셔너리 키값에 없다면)
            elif self.inserted_money not in person.my_money_dict:          
                print '\n--------------------'
                print '잘못된 돈을 넣으셨습니다. 올바른 돈을 넣어주시기 바랍니다.'
                print '100, 200, 500, 1000, 5000'
                self.inserted_money = 0

            #예외처리2 : 잔액이 부족(나의 딕셔너리 key의 val이 0이라면)
            elif person.my_money_dict[self.inserted_money] == 0:
                print '\n--------------------'
                print '넣으신 돈의 잔액(수)가 부족합니다.'
                print '다시 한번 확인해 주세'
                self.inserted_money = 0
       
            # 종료조건이 아니고, 예외상황이 아닐 경우 정상적인 실해
            else:

                #투입한 만큼 지갑에서 돈을 뺀다. (해당 돈의 갯수에서 하나 빼기)
                person.my_money_dict[self.inserted_money] -= 1

                #누적해서 투입된 돈의 합을 표시한다.
                self.inserted_money_sum += self.inserted_money
                print '지금까지 %d가 투입되었네요' % self.inserted_money_sum

        #투입된 돈의 총 합이 0이상이 아니면..입금이 안된 것임
        if self.inserted_money_sum <= 0: 
            print '돈이 입금되지 않았네요. 프로그램 종료 합니다'

        #현재까지 투입된 돈 보여주기
        print '지금까지 %d가 투입되었네요' % self.inserted_money_sum

    #음료수 고르기
    def ready_get_product(self, person, my_money_dict):
        print '\n--------------------'
        print '구매가능 음료수'
        for key in self.products_dict:
            print key, '가격 %d, 수량%d' % (self.products_dict[key]['price'], self.products_dict[key]['number'])
        
        while(True):
            #음료수 선택
            self.choice_product = raw_input('\n 드실 음료수를 선택해주세요 : ')

            #예외처리1 : 올바른 상품을 선택하지 않았을 경우
            if self.choice_product not in self.products_dict:
                print '올바른 상품을 선택하지 않으셨습니다.'
                print '상품을 다시 골라주시기 바랍니다'

            #예외처리2 : 수량이 부족한 경우
            elif self.products_dict[self.choice_product]['number'] ==0:
                print '수량이 부족합니다'
                print '다른 상품을 골라주세요'

            #예외처리3 : 금액이 부족한 경우 (돈넣는 함수 실행)
            elif self.products_dict[self.choice_product]['price'] > self.inserted_money_sum:
                print '잔액이 부족합니다.'
                self.get_inserted_money(person, my_money_dict)

            #예외처리4: 금액이 부족한 경우2(다시 뽑아먹을때 남은 잔액과 비교) re_try 1 & 잔액부족
            elif (self.re_try == 1) & (self.products_dict[self.choice_product]['price'] > self.change):
                print '잔액이 부족합니다.'
                self.get_inserted_money(person, my_money_dict)                

            else:
                break

        #상품수령 함수실행
        self.get_product(person, my_money_dict)

    def get_product(self, person, my_money_dict):
        print '\n상품이 나왔습니다'
        print self.choice_product
        print '---------------------'

        #기계 수량체크
        self.products_dict[self.choice_product]['number'] -= 1

        #잔돈반환여부
        self.change = self.inserted_money_sum - self.products_dict[self.choice_product]['price']
        print '남은 잔액 %d' % self.change

        while(True):
            self.re_try = input('다른 상품을 고르시겠습니까? (yes : 1, no : 0) : ')

            if self.re_try ==0:
                print '반환금액 %d' % self.change
                print '이용해주셔서 감사합니다'
                break

            #상품선택 함수 호출
            elif self.re_try == 1:
                self.ready_get_product(person, my_money_dict)
                break

            #예외처리(다시 선택)
            else:
                print '입력이 잘못되었습니다. 다시 시도해주세요.'


# 메인 로직
if __name__ == '__main__':

    #오브젝트(인스턴스) 생성 : person & machine
    youngnam = person()
    nhn_next = machine()

    #돈 투입하기 (투입하는 사람, 투입한 사람의 돈 딕셔너리 인자값으로 취)
    nhn_next.get_inserted_money(youngnam, youngnam.my_money_dict)
    nhn_next.ready_get_product(youngnam, youngnam.my_money_dict)








