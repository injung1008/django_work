'''
구구단 프로그램은 단을 입력받아서. 입력받은 단의 1-9의 출력하는 어플이다.
단. 단은 정수이다



class Gugudan(object):
    number = 0 # 단은 정수다 라는 개념


    def mul(self):
        for i in range(1,10):
            print(f'{i} * {self.number} = {i * self.number}')


    @staticmethod
    def main():
        gugu = Gugudan()
        while 1:

            menu = int(input('0:exit, 1: input, 2:ourput'))
            if menu == 0:
                break
            elif menu == 1 :
                gugu.number = int(input(f'단입력')) # 프로퍼티로 직접 값을 넣어줌 () 없는건 메소드가 아니기 때문
                gugu.mul()

            else:
                continue


Gugudan.main()

'''
class Gugudan(object):
    number = 0
    dict = {}
    def mul(self):
        for i in range(2, 10):
            print(f'{i}*{self.number} = {i * self.number}')



    def mul_fix(self):
        for i in range(2,10):
            for dan in range(1,10):
                print(f' {i} * {dan} = {i * dan}')

    def print_dict_dan(self):
        d = self.dict
        for i in range(1,10): # 키는 유니크 하기 때문에 고정된 단(dan)이 아니라, 숫자다  1-9까지 변화하는 값이 키가 되어야 함
            d[i] = self.number * i
        print('딕셔너리 출력')
        print(d)
        for k in d.keys():
            print(f'{self.number} * {k} = {d.get(k)}')





    @staticmethod
    def main():
        gugu = Gugudan()
        while 1 :
            menu = int(input('1: input, 2: fix 3: dix'))
            if menu == 1:
                gugu.number = int(input('단입력'))
                gugu.mul()
            elif menu == 2:
                gugu.mul_fix()
            elif menu == 3:
                gugu.number = int(input('단입력'))
                gugu.print_dict_dan()

Gugudan.main()

