'''
class Conversion(object):
    dic = {} # 프로퍼티
    ls = []
    tp = ()
    s = ''
    i = 0
    f = 0.0

    def create(self):
        self.tp = tuple(range(1,11))
        return self.tp
    
    #return과 self 는 같이 사용 하는것이 비효율적이다 그렇기 때문에 return 으로 바로 처리 해버린다 return은 한번 사용하고 버린다는 개념으로 설명하는 것이기 때문에 


    def c_create(self):
        self.ls = list(self.tp)
        return self.ls

    def fl(self):
        self.ls = [float(self.ls[i]) for i in self.ls]
        return self.ls

    def change(self):
        self.ls = [int(self.ls[i]) for i in self.ls]
        return self.ls

    def c_dic(self):
        for i, j in zip(self.ls,self.ls):
            self.dic[str(i)] = j
        return self.dic

    def hel(self):
        self.tp = tuple('hello')
        return self.tp

    def c_hel(self):
        self.ls = list(self.tp)
        return self.ls

    @staticmethod
    def main():
        c = Conversion()
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                print(f'튜플 : {c.create()}')
            elif m == '2':
                print(c.c_create())
            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '3':
                print(c.fl())
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '4':
                print(c.change())
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '5':
                print(c.c_dic())
            # 4번 리스트를 딕셔너리로 전환하시오. 단 키는 리스트의 인덱스인데 str 로 전환하시오 (return)
            elif m == '6':
                print(c.hel())
            # 'hello' 를 튜플로 전환하시오
            elif m == '7':
                print(c.c_hel())
            # 6번 튜플을 리스트로 전환하시오

            else:
                continue


Conversion.main()







'''
import pandas as pd

class Conversion(object):

    @staticmethod
    def create_tuple() -> ():
        return (1,2,3,4,5,6,7,8,9)


    @staticmethod
    def tuple_to_list(tp) -> []:  #self를 쓰지 않기때문에 프로퍼티를 쓰지 않는다 그렇기 떄문에 객체가 아니다
        return list(tp)


    @staticmethod
    def int_to_float(ls) -> []:
        return [float(i) for i in ls]
    @staticmethod
    def float_to_int(ls) -> []:
        return [int(i)for i in ls]
    @staticmethod
    def list_to_dictionary(ls) -> {}:
        return dict(zip([str(i) for i in ls], ls))

    @staticmethod
    def hello_to_tuple(st) -> ():
        return tuple(list(st))

    @staticmethod
    def hello_to_list(tp) -> []:
        return list(tp)

    @staticmethod
    def dictionary_to_dataframe(dt) -> object:
        return pd.DataFrame.from_dict(dt, orient = 'index')




    @staticmethod
    def main():
        c = Conversion()
        tp = ()
        ls = []
        while 1:
            m = input('0-exit 1-create tuple\n'
                      '2-convert list\n'
                      '3-convert float-list\n'
                      '4-convert int-list\n'
                      '5-list convert dictionary\n'
                      '6-str convert tuple\n'
                      '7-str tuple convert list')
            if m == '0':
                break
            # 1부터 10까지 요소를 가진 튜플을 생성하시오 (return)
            elif m == '1':
                print(f'튜플 : {c.create()}')
            elif m == '2':
                tp = c.create_tuple()
                print(f' tp 타입 : {type(ls)}')
                print(ls)

            # 1번 튜플을 리스트로 전환하시오 (return)
            elif m == '3':
                ls = c.int_tofloat(ls)
                print(f' {type(ls)}')
                print(ls)
            # 2번 리스트를 실수(float) 리스트 바꾸시오  (return)
            elif m == '4':
                ls = c.float_to_int(ls)
                print(f' {type(ls)}')
                print(ls)
            # 3번 실수(float) 리스트을, 정수 리스트로 바꾸시오  (return)
            elif m == '5':
                dt = c.list_to_dictionary(ls)
                print(f'dt의 타입 : {type(dt)}')
                print(dt)
                # 'hello' 를 튜플로 전환하시오
            elif m == '6':
                tp = c.hello_to_tuple('hello')
                print(f'tp의 타입 : {type(tp)}')
                print(tp)
                # 6번 튜플을 리스트로 전환하시오
            elif m == '7':
                ls = c.tuple_to_list(tp)
                print(f'ls의 타입 : {type(ls)}')
                print(ls)
                # 5번 딕셔너리를 데이터프레임 으로 전환하시오
            elif m == '8':
                tp = c.create_tuple()
                ls = c.tuple_to_list(tp)
                dt = c.list_to_dictionary(ls)
                print(dt)
                df = c.dictionary_to_dataframe(dt)
                print(f'df의 타입 : {type(df)}')
                # If using all scalar values, you must pass an index
                print(df)

            else:
                continue

Conversion.main()