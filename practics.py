import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

class NaverMovie(object):
    url = 'https://vibe.naver.com/chart/total'
    driver = 'C:/Program Files/Google/Chrome/chromedriver'
    dict = {}
    ls = []

    def scrap(self):
        chromedriver = webdriver.Chrome(self.driver)
        chromedriver.get(self.url)
        soup = BeautifulSoup(chromedriver.page_source, 'html.parser')
        all_div = soup.find_all(name = 'span', attrs= ({'class':'inner_cell'}))
        for i, j in enumerate(all_div):
            print(f'{i+1} . {j.find("a").text}')
            self.ls.append(j.find("a").text)
        chromedriver.close()

    def to_dict(self):
        for i, j in enumerate(self.ls):
            self.dict[str(i)] = j
        print(self.dict)
        for k in self.dict.keys():
            print(f'{k} : {self.dict.get(k)}')

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient = 'index')
        print(self.df)
    def dict_to_csv(self):
        path = './party/movie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')



if __name__ == '__main__':
    naver = NaverMovie()
    naver.scrap()
    naver.to_dict()
    naver.dict_to_dataframe()
    naver.df_to_csv()


