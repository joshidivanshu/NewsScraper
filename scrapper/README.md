## News Scraping using celery
### Running on Local Machine
```angular2html
git clone https://github.com/joshidivanshu/
```
```angular2html
pip install -r requirements.txt
```
```angular2html
python manage.py migrate
```
```angular2html
python manage.py runserver
```
### To run celery workers
```angular2html
celery -A mysite scrapper -l info
```
### To run & install RabbitMQ using Docker
```angular2html
docker run rabbitmq
```

### To check the news
```angular2html
localhost:8000/news
```


### To check the movie data
```angular2html
localhost:8000/movie
```


