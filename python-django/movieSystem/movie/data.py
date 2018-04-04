# 引用库

import requests
import re
from bs4 import BeautifulSoup
import time



import subprocess
import os
from django.core.wsgi import get_wsgi_application
import sys
sys.path.extend(['D:\\github\\movie-recommendation-system\\python-django\\movieSystem',])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movierecomend.settings")
application = get_wsgi_application()
import django
django.setup()
from movie.models import *

# 设置headers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

# 设置url
urls = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,225,25)]

# 获得url的电影
def get_url_movie(url):
    payload = {'filter':''}
    response = requests.get(url,headers=headers,params=payload)
    soup = BeautifulSoup(response.text,'lxml')
    movie_hrefs = soup.select('div.pic > a')
    for movie_href in movie_hrefs:
        get_info_movie(movie_href['href'])
    time.sleep(2)

# 获得电影详情
def get_info_movie(url):
    response = requests.get(url,headers=headers)
    if(response.status_code!=404):
        soup = BeautifulSoup(response.text,'lxml')
        name = soup.select('div#content > h1 > span')[0].get_text()
        brief = soup.find_all("span", attrs={"property": "v:summary"})[0].get_text().strip()
        rate = soup.find_all("strong", attrs={"property": "v:average"})[0].get_text()
        link = re.findall('<span class="pl">IMDb链接:</span>[^"]*"(.*?)"',response.text,re.S)[0]
        img = soup.find_all("img", attrs={"rel": "v:image"})[0]['src']
        create_date = soup.find_all("span", attrs={"property": "v:initialReleaseDate"})[0].get_text()
        #type_str = '/'.join(genre.text for genre in soup.findAll('span',property='v:genre'))       
        print(name,brief,rate,link,img,create_date)
        Film.objects.get_or_create(
            name = name,
            brief = brief,
            rate = rate,
            link = link,
            img = img,
            create_date = create_date
        )
        print("》》》插入电影成功！")
        



for url in urls:
    get_url_movie(url)
