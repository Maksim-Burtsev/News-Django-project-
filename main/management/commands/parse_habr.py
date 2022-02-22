from django.core.management.base import BaseCommand
from django.utils import timezone

import requests
from bs4 import BeautifulSoup
import fake_useragent
import datetime

from main.models import Post


def get_articles_from_page(url):
    
    user = fake_useragent.UserAgent().random
    header = {
        'user-agent': user,
    }
        
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')

    div = soup.find('div', {'class' : 'tm-articles-subpage'})

    articles = div.find_all('article')

    return articles

def get_post_data(article):
    try:
        title = article.find('a', {'class' : 'tm-article-snippet__title-link'}).text
    except:
        return False

    try:
        summary = article.find('p').text
    except:
        summary = article.find('div', {'class' : 'article-formatted-body article-formatted-body_version-1'}).text

    time = datetime.datetime.strptime(
        article.find('time').get('title'), 
        '%Y-%m-%d, %H:%M', 
        )

    cat_id = 1

    url = 'https://habr.com' + article.find('a', {'class' : 'tm-article-snippet__title-link'}).get('href')

    image = ''
    images = article.find_all('img')
    if len(images) == 0:
        return False
    elif len(images) == 1:
        image = images[0].get('src')
    else:
        image = images[1].get('src')

    return (title, summary, time, cat_id, url, image)

def create_db_entry(data, post_id):
    
    title, content, time_published, cat_id, url, img = data

    time_published = time_published.astimezone(timezone.utc)

    obj = Post.objects.get(id=post_id)

    obj.title = title
    obj.content = content
    obj.time_published = time_published
    # obj.cat_id = cat_id
    obj.url = url
    obj.image_link = img

    obj.save()
    # obj = Post(
    #     title = title,
    #     content = content, 
    #     time_published = time_published,
    #     cat_id = cat_id, 
    #     url = url,
    #     image_link = img,
    #     id = post_id, 
    # )

    # obj.save()

def main():
    
    URL = 'https://habr.com/ru/all/page'
    post_id = 1

    for i in range(1, 6):
        url = URL + str(i) + '/'
        articles = get_articles_from_page(url)
        for j in range(len(articles)):
            data = get_post_data(articles[j])
            if data:
                create_db_entry(data, post_id)
                post_id += 1
            else:
                pass
            print(f'{j+1}/{len(articles)}')
            
        print(f'{i}/5')
class Command(BaseCommand):
    help = "Парсер Хабра"

    def handle(self, *args, **kwargs):
        main()

