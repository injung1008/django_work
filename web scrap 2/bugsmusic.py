from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic():

    url = ''
    # init이 제거된것이아니라 파라미터가 없는 생성자(bugs = BugsMusic())가 필요하면 생략가능.
    # 표기가 생략되었을뿐 , self.url = url 이것과 같다



    def __str__(self):
        return self.url

    @staticmethod
    def del_element(soup, value):

        for i in soup.find_all(name='p', attrs=({"class" : value})):
            count = 0
            count += 1
            print(f'{str(count)} ranking')
            print(f'{value}: {i.find("a").text}')


    #'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210524&charthour=15'
    @staticmethod
    def main():
        bugs = BugsMusic()

        while True:
            menu = int(input('0:exit, 1:Input URL, 2:get Ranking ,3: 실행'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('input url')

            elif menu == 2:
                print(f'input url is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                print('_______________artist ranking__________________')
                bugs.del_element(soup, 'artist')
                print('_______________title ranking__________________')
                bugs.del_element(soup, 'title')



            else:
                print('오류')
                continue


BugsMusic.main()


'''
                for i in soup.find_all(name = 'p',attrs=({"class":"artist"})): # p class="title" adult_yn>0
                    count = 0
                    count +=1
                    print(f'{str(count)} ranking')
                    print(f'artist: {i.find("a").text}')


                print('_______________title ranking__________________')
                for i in soup.find_all(name = 'p',attrs=({"class":"title"})):
                    count = 0
                    count +=1
                    print(f'{str(count)} ranking')
                    print(f'title: {i.find("a").text}')
'''