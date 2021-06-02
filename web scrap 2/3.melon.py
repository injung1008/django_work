import pandas as pd
import requests
from bs4 import BeautifulSoup
class Melon():
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    count = []
    total_ls = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}',headers=self.headers).text
        # 이건 오로지 시간 time 을 받기 위한 함수 ? 인지  {self.url} 이건 위에 있는  url을 호출 하는 기능인가 ?


    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------제목-------')
        n_title = 0

        ls = soup.find_all('div', {"class":self.class_name[0]})
        n_title +=1
        for i in ls:
            print(f'{str(n_title)} ranking ')
            print(f'{i.find("a").text}')
            self.title_ls.append(i.find("a").text)

        print('------가수-------')
        ls = soup.find_all('div', {"class": self.class_name[1]})
        for i in ls:
            print(f'{i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def insert_title_dict(self):

        for i in range(0,len(self.title_ls)):
            self.dict[i] = self.title_ls
        print(self.dict)
        for k in self.dict.keys():
            print(f'{k} : {self.dict.get(k)}')

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient = 'index')
        print(self.df)
    def df_to_csv(self):
        path = './data/melon.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN', mode = 'w')

    @staticmethod
    def main():
        melon = Melon()
        while 1 :
            menu = int(input('0, 1:input 2: output'))
            if menu == '0':
                break
            if menu == 1:
                melon.set_url(input('스크래핑 할 날짜 입력'))  # '2021052511'
            elif menu == 2:
                melon.class_name.append('ellipsis rank01')
                melon.class_name.append('ellipsis rank01')
                melon.get_ranking()
            elif menu == 3:
                melon.insert_title_dict()
            elif menu == 4:
                melon.dict_to_dataframe()
            elif menu == 5:
                melon.df_to_csv()
            else:
                print('Wrong number')
                continue


Melon.main()



'''


'''






