# -*- coding: UTF-8 -*-
dict_students = {
                    '김경식' : { 
                        'basic' : {'age' : 24, 'key' : '9005102123112', 'nationality' : 'korea' ,'address' : '서울시 강동구 상일동'},
                        'other' : {'courses' : ['ciritical Thinking','프로그래밍연습','자구알','NEXT소프트개론','기초수학','인문사회학1','확률과 통계'], 
                                   'features' : '몽고메리',
                                   'recover' : '4-10',
                                   'hobby' : '암벽등반' }
                    },

                    '김영' : { 
                        'basic' : {'age' : 20, 'key' : '9402231122121', 'nationality' : 'england' ,'address' : '서울시 도곡동 타워팰리스 304호'},
                        'other' : {'courses' : ['UX디자인 1','critical Thinking','프로그래밍 연습','휴먼디자인','인문사회학2','자구알'], 
                                   'features' : '0을 의미한다',
                                   'recover' : '3-9',
                                   'hobby' : '철권' }
                    },

                    '김우진' : {
                        'basic' : {'age' : 24, 'key' : '9001141233222', 'nationality' : 'America' ,'address' : '판교학교근처어딘가'},
                        'other' : {'courses' : ['ciritical Thinking','프로그래밍 연습','휴먼디자인','기초수학','인문사회학1','확률과 통계'], 
                                   'features' : '귀여운 목소리',
                                   'recover' : '3-8',
                                   'hobby' : '기타연주' }
                    },

                    '김성환' : { 
                        'basic' : {'age' : 20, 'key' : '9403123311112', 'nationality' : 'korea' ,'address' : '경기도 수원시 장안구'},
                        'other' : {'courses' : ['ciritical Thinking','게임제작개론','NEXT소프트개론','기초수학','인문사회학1','확률과 통계','Business English','프로그래밍연습'], 
                                   'features' : 'smile!',
                                   'recover' : '2-6',
                                   'hobby' : '벚꽃놀이' }
                    },
                    '김남훈' : { 
                        'basic' : {'age' : 19, 'key' : '9507212211201', 'nationality' : 'France' ,'address' : '서울시 영등포구 문래3가'},
                        'other' : {'courses' : ['ciritical Thinking','소프트웨어공학','NEXT소프트개론','기초수학','인문사회학1','확률과 통계'], 
                                   'features' : '유희열',
                                   'recover' : '3-9',
                                   'hobby' : '기자활동' }
                    },
                    '김희재' : { 
                        'basic' : {'age' : 21, 'key' : '8504111123112', 'nationality' : 'Mars' ,'address' : '서울시 용산구 갈월동 87번지'},
                        'other' : {'courses' : ['ciritical Thinking','NEXT소프트개론','UX디자인1','기초수학','인문사회학1','자구알','프로그래밍 연습','확률과 통계'], 
                                   'features' : '보스',
                                   'recover' : '4-10',
                                   'hobby' : '웹개발' }
                    },
                    '윤지수' : { 
                        'basic' : {'age' : 29, 'key' : '8503211123112', 'nationality' : 'korea' ,'address' : '경기도 광명시 하안2동 698번지'},
                        'other' : {'courses' : ['ciritical Thinking','NEXT소프트개론','UX디자인1','Business English','물리학','자구알','프로그래밍 연습','확률과 통계'], 
                                   'features' : '혼자웃기',
                                   'recover' : '3-8',
                                   'hobby' : 'sleeping' }
                    }
                }


def check_students(find_class):
  new_dict = {}
  num = 0

  for name in dict_students:
    for courses_list in dict_students[name]['other']['courses']:
      if courses_list == find_class:
        print new_dict[name][other]['recover']
'''
        if dict_students[name][other]['recover'] not in new_dict:
          dict_students[name][other]['recover'] = 1
        else:
          new_dict[name][other]['recover']

'''

find_class = raw_input("어떤 강의의 학생수를 알고 싶으신가요? : ")
check_students(find_class)


