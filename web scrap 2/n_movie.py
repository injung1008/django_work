import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


class NaverMovie(object):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    c_class = ''
    driver = 'C:/Program Files/Google/Chrome/chromedriver'
    dict = {}
    ls = []

    def scrap(self):
        chromedriver = webdriver.Chrome(self.driver)
        chromedriver.get(self.url)  #url을 드라이버에 넣어줌
        soup = BeautifulSoup(chromedriver.page_source, 'html.parser')
        all_div = soup.find_all(name = 'div', attrs = ({'class': self.c_class}))
        for i, j in enumerate(all_div):
            print(f'{i+1}.{j.find("a").text}')
            self.ls.append(j.find("a").text)
        chromedriver.close()

    def insert_title_dict(self):
        for i, j in enumerate(self.ls):
            self.dict[str(i)] = j
        print(self.dict)
        for k in self.dict.keys():
            print(f'{k} : {self.dict.get(k)}')

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt,orient= 'index')
        print(self.df)
    def df_to_csv(self):
        path = './party/movie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

if __name__ == '__main__':
    naver = NaverMovie() #  naver(인스턴스) = NaverMovie() 인스턴스는 생성자에 의해서 만들어진 결과물
    naver.c_class = input(f'tit3를 넣어주세요')
    naver.scrap()  # while 문 스태틱  익숙해 져서, 생략하고 바로 진행  생성자로 사용
    naver.insert_title_dict()
    naver.dict_to_dataframe()
    naver.df_to_csv()






