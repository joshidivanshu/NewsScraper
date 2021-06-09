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


### Project Snaps
![Screenshot from 2021-06-09 19-05-21](https://user-images.githubusercontent.com/32302492/121365090-fb45f080-c955-11eb-97e0-e27a2c607a39.png)
![Screenshot from 2021-06-09 19-05-30](https://user-images.githubusercontent.com/32302492/121365104-fd0fb400-c955-11eb-8b1e-df2312d71573.png)
![Screenshot from 2021-06-09 19-05-36](https://user-images.githubusercontent.com/32302492/121365113-fed97780-c955-11eb-916b-d9114029af54.png)
![Screenshot from 2021-06-09 19-06-05](https://user-images.githubusercontent.com/32302492/121365119-000aa480-c956-11eb-9182-b099e14d54a3.png)


