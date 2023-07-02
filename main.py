import sqlite3

import requests
from bs4 import BeautifulSoup


class Parse:
    url = "https://gorzdrav.org/blog/"
    #url2 пока надо менять в ручную
    url2 = "https://gorzdrav.org/blog/?page=12"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url2, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    items = soup.find_all('div', class_='c-blog-list__item')
    names = []
    args = []


    def parser_names(self):

        for i in Parse.items:
            Parse.names.append(i.find('a', class_='c-blog-list__item-title').get_text(strip=True))


    def parser_list(self):
        url_list = []
        for i in Parse.items:
            url_name = i.select_one('a', class_='c-blog-list__item-image')['href']
            url_list.append(Parse.url + url_name.replace('/blog/', ''))


        for i in url_list:
            arrgs = []
            response = requests.get(url=i, headers=Parse.headers)
            soup = BeautifulSoup(response.content, 'lxml')
            name1 = soup.find_all('p')
            for o in name1:
                arrgs.append(o.text)
            Parse.args.append(" ".join(arrgs)[:-267])
            arrgs.clear()

        for ar in Parse.args:
            print(ar, '\n')

par = Parse()
par.parser_names()
par.parser_list()

db = sqlite3.connect("mydb.db")
cursor = db.cursor()
g = 0

while g <= 19:
    b = (Parse.names[g])
    c = (Parse.args[g])
    cursor.execute("INSERT INTO Posts (name, description) VALUES (?, ?)", (b, c))
    db.commit()
    g += 1
db.close()



