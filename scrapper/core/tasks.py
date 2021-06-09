from celery import shared_task
from bs4 import BeautifulSoup
from requests import get
from .models import WorldNews, IndiaNews, BusinessNews, Movie


@shared_task
def india_today_world():
    pages = [str(i) for i in range(0, 5)]
    WorldNews.objects.all().delete()

    for i in pages:
        url = 'https://www.indiatoday.in/world?page='+i
        response = get(url) 
        data = BeautifulSoup(response.text, 'html.parser')
        news_data = data.find_all('div', class_ = 'detail')
        print('------page no'+i+'--------------')
        for i in range(len(news_data)):
            print(news_data[i].a.text)
            obj = WorldNews(data=news_data[i].a.text)
            obj.save()


india_today_world()


@shared_task
def india_today_business():
    pages = [ str(i) for i in range(0, 5)]
    BusinessNews.objects.all().delete()

    for i in pages:
        url = 'https://www.indiatoday.in/business?page='+i
        response = get(url) 
        data = BeautifulSoup(response.text, 'html.parser')
        news_data = data.find_all('div', class_ = 'detail')
        print('------page no'+i+'--------------')
        for i in range(len(news_data)):
            print(news_data[i].a.text)
            obj = BusinessNews(data = news_data[i].a.text)
            obj.save()


india_today_business()


@shared_task
def india_today():
    pages = [ str(i) for i in range(0, 5)]
    IndiaNews.objects.all().delete()

    for i in pages:
        url = 'https://www.indiatoday.in/india?page='+i
        response = get(url) 
        data = BeautifulSoup(response.text, 'html.parser')
        news_data = data.find_all('div', class_ = 'detail')
        print('------page no'+i+'--------------')
        for i in range(len(news_data)):
            print(news_data[i].a.text)
            obj = IndiaNews(data=news_data[i].a.text)
            obj.save()


india_today()


@shared_task
def movie_data():
    years_url = [str(i) for i in range(2000, 2018)]
    for year_url in years_url:
        response = get('https://www.imdb.com/search/title?release_date=' + year_url +
        '&sort=num_votes,desc&page=1')
        page_html = BeautifulSoup(response.text, 'html.parser')

        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        for container in mv_containers:
            obj = Movie()
            if container.find('div', class_ = 'ratings-metascore') is not None:
                obj.name = container.h3.a.text
                obj.year = container.h3.find('span', class_ = 'lister-item-year').text
                obj.imdb = container.strong.text
                obj.metascores = int(container.find('span', class_ = 'metascore').text)
                obj.votes = container.find('span', attrs = {'name':'nv'})['data-value']
                obj.save()
                print("data added")
        print("completed successfully")

# movie_data()


@shared_task
def refresh_info():
    india_today_world()
    india_today_business()
    india_today()
