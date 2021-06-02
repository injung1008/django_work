import requests
from bs4 import BeautifulSoup
class Melon():

    url = ''


    def __str__(self):
        return self.url



    @staticmethod
    def main():
        mel = Melon()



        while True:
            menu = int(input("0: exit,1 : input 2: get rank"))
            if menu == 0:
                break

            elif menu == 1:
                mel.url = input('input url')

            elif menu == 2:
                print(f'input url is {mel}')
                headers = {'User-Agent': 'Mozilla/5.0'}
                url = "https://www.melon.com/chart/day/index.htm"
                res = requests.get(url, headers=headers).text
                soup = BeautifulSoup(res, 'lxml')
                print('_______________title ranking__________________')
                n_title = 0
                for link1 in soup.find_all(name = 'div', attrs=({"class":"ellipsis rank01"})):
                    n_title +=1
                    print(f'{str(n_title)} ranking ')
                    print(f'title: {link1.find("a").text}')

                print('_______________artist ranking__________________')
                n_artist = 0
                for link1 in soup.find_all(name='div', attrs=({"class": "ellipsis rank02"})):
                    n_artist += 1
                    print(f'{str(n_artist)} ranking ')
                    print(f'artist: {link1.find("a").text}')


            else:
                print('오류')
                continue


Melon.main()










