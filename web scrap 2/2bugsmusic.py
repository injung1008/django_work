from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic():

    url = ''
    class_name = []
    # init이 제거된것이아니라 파라미터가 없는 생성자(bugs = BugsMusic())가 필요하면 생략가능.
    # 표기가 생략되었을뿐 , self.url = url 이것과 같다



    def __str__(self):
        return self.url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        print("< ARTIST >")
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[0]})):  # "artist"
            count += 1
            print(f'{str(count)} RANKING')
            print(f'artist: {i.find("a").text}')
        print("< TITLE >")
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):  # "title"
            count += 1
            print(f'{str(count)} RANKING')
            print(f'title: {i.find("a").text}')


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
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.scrap()


            else:
                print('오류')
                continue


BugsMusic.main()

