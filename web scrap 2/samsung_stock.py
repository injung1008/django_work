import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


class Samsung(object):
    url = 'https://finance.naver.com/item/sise_day.nhn?code=005930&page=1'
    ls = []
    driver = 'C:/Program Files/Google/Chrome/chromedriver'


    def get_stock(self):
        c_chrome = webdriver.Chrome(self.driver)
        c_chrome.get(self.url)
        soup = BeautifulSoup(c_chrome.page_source, 'html.parser')
        ls = soup.find_all(name = 'td', attrs=({'class':'num'}))
        # news_rows = soup.find('table', class_='type2').find_all('td', class_='title')
        for i in ls:
            print(f' {i.find("span").text}')

        c_chrome.close()


if __name__ == '__main__':
    samsung = Samsung()
    samsung.get_stock()
























