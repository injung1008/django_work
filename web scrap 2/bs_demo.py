from bs4 import BeautifulSoup
class BsDemo():
    html_doc= ''

    def __str__(self):
        return self.html_doc

    @staticmethod
    def main():
        bs = BsDemo()
        while True:
            m = input('1:input, 2:all html pirnt 3: print_title ')

            if m == '1' :
                bs.html_doc =''' <html><head><title>The Dormouse's story</title></head>
                                <body>
                                <p class="title"><b>The Dormouse's story</b></p>

                                <p class="story">Once upon a time there were three little sisters; and their names were
                                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                and they lived at the bottom of a well.</p>

                                <p class="story">TEST VALUE</p>
                                '''
            elif  m == '2':
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.prettify())

            elif m == '3':
                soup = BeautifulSoup(bs.html_doc, 'html.parser')
                print(soup.title.string) # 프로퍼티, 속성이기 때문에 () 없다 / string은 자연어


BsDemo.main()
