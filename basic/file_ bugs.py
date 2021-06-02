import pandas as pd
from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls= []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        print('------- 제목 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[1]}))
        for i in ls:
            print(f' {i.find("a").text}')
            self.title_ls.append(i.find("a").text)
        print('------ 가수 --------')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            print(f'{i.find("a").text}')
            self.artist_ls.append(i.find("a").text)

    def insert_title_dict(self):

        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        print(self.dict)
        for k in self.dict.keys():
            print(f'{k}:{self.dict.get(k)}') # (f'{k - 키값 }:{self.dict.get(k)} - 밸류 정해진 공식 ')

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN', mode = 'w')




    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output 3 - dix')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url(input('상세정보 입력')) # wl_ref=M_contents_03_01
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()

            elif menu == '4':
                bugs.dict_to_dataframe()
            elif menu == '5':
                bugs.df_to_csv()


            else:
                print('Wrong Number')
                continue

BugsMusic.main()