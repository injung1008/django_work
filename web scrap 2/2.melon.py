import requests
from bs4 import BeautifulSoup
class Melon():
    url = ''



    def __str__(self):
        return self.url
    @staticmethod
    def get_ranking(soup,value):
        for i in soup.find_all(name='div', attrs=({"class": value})):
            count = 0
            count += 1
            print(f'{str(count)} ranking')
            print(f' title = {i.find("a").text}')




    @staticmethod
    def main():
        melon = Melon()
        while True:
            menu = int(input('0:exit, 1: input URL, 2: get rank'))

            if menu == 0:
                break

            elif menu == 1:
                print(f' URL = {melon}')
                melon.headers = {'User-Agent': 'Mozilla/5.0'}
                melon.url = "https://www.melon.com/chart/day/index.htm"
                melon.res = requests.get(melon.url, headers=melon.headers).text
                soup = BeautifulSoup(melon.res, 'lxml')
                print('---------------title ranking---------------')
                melon.get_ranking(soup,"ellipsis rank01" )
                print('---------------artist ranking---------------')
                melon.get_ranking(soup,"ellipsis rank02" )


Melon.main()




