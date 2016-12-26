import urllib2
from bs4 import BeautifulSoup
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

url_1 = 'http://www.usst.edu.cn/s/1/t/517/p/2/i/382/list.htm'
page = url_1[-12:-9]
for i in range(1,int(page)):
    url = "http://www.usst.edu.cn/s/1/t/517/p/2/i/{0}/list.htm" . format(i)
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, from_encoding = 'utf-8')
    hotNews = soup.find_all('div', {'class', 'column_list_content'})[0].find_all('tr')
    f = open(r'd:/xinwen.txt','a')
    for i in hotNews:
        f.write('\n' + i.a.text)
        print i.a.text
        print i.a['href']
    f.close()
