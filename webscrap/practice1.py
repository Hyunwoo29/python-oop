from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):
    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def ranking(element, soup):
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": element})):
            count += 1
            print(f'순위: {str(count)}')
            print(f'{element}: {i.find("a").text}')

    """https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01"""
    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input("0.Exit 1.Input URL 2.Get Ranking 3.Update 4.Delete"))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URL')
            elif menu == 2:
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url),'lxml')

                print('--------------- ARTIST RANKING-----------------')
                BugsMusic.ranking('artist', soup)
                BugsMusic.ranking('title', soup)


            elif menu == 3:
                pass
            else:
                print("wrong number")
                continue
BugsMusic.main()