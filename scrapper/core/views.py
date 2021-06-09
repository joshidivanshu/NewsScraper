from django.shortcuts import render
from .models import IndiaNews, BusinessNews, WorldNews, Movie
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def movies(request):
    movie1 = Movie.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(movie1, 20)
    try:
        movie = paginator.page(page)
    except PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'movie': movie})


def news(request):
    india_news = IndiaNews.objects.all()
    world_news = WorldNews.objects.all()
    business_news = BusinessNews.objects.all()
    return render(request, 'news.html', {'india': india_news, 'world': world_news, 'business': business_news})


def base(request):
    return render(request, 'base.html')
