from bs4 import BeautifulSoup
import requests
class BugsMusic(object):
    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text
    def get_ranking(self):
        soup = BeautifulSoup(set.url, 'lxml')
        ls1 = soup.find_all(name = 'p', attrs = ({"class": self.class_name{1}}))
        ls2 = soup.find_all(name = 'p', attrs = ({"class": self.class_name{0}}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        for i in ls2:
            self.artist_ls.append(i.find("a").text)

    def insert_title_dict(self):
        #방법1
        for i in range(0, len(self.title_ls)):            # len(self.title_ls) 타이틀 길이 만큼 돌려라
            self.dict[self.title_ls[i]] = self.artist_ls[j] # self.dt['tom'- 키값 ] = 100 - 밸류
        # 방법2
        for i,j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        # 방법3
        for i,j in enumerate(self.title_ls):
            self.dict[self.title_ls[j]] = self.artist_ls[i]

        print(dict)


    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time, 2-output, 3-print dict')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('wl_ref=M_contents_03_01')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_title_dict()
            else:
                print('Wrong Number')
                continue
BugsMusic.main()