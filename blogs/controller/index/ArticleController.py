from django.http import HttpResponse, Http404
from blogs.models import Article
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os, django
import requests


# Create your views here.
def index(request):
    queryLimit = {
        'id': 1,
        'article_name': 'sb',
        'author_name': 'pl',
        'release_start_time': '2017-07-02',
        'release_end_time': '2017-08-03'
    }
    # request.GET.get('queryLimit')
    selectLimit(queryLimit)
    article_datas = Article.objects.all()
    paginator = Paginator(article_datas, 5)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    context = {
        "latest_article_list": contacts
    }
    return render(request, 'blogs/index.html', context)


def detail(request, article_id=0):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404('article does not exist')
    return render(request, 'blogs/single.html', {'article': article})


def update(request, article_id=0):
    return HttpResponse("article update with article_id:" + article_id)


def delete(request, article_id=0):
    return HttpResponse("article delete with article_id:" + article_id)


# queryLimit = {
# 'id':xx,
# 'article_name':xx,
# 'author_name':xx,
# 'release_start_time':xx,
# 'release_start_time':xx
# }
def selectLimit(queryLimit):
    queryLimit = getParams(queryLimit)
    print(queryLimit)
    exit()
    if queryLimit.has_key('id') and queryLimit.get('id') is not None:
        Article.objects.filter(id=queryLimit.get('id'))


def getParams(params):
    kargs = {}
    for (k, v) in params.items():
        if v is not None:
            kargs['k'] = v
    return kargs


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    url = 'http://all_product_services.com/100009369'
    data = requests.get(url)
    print(data)
    exit()

    queryLimit = {'id': 1, 'name': 'pl'}
    selectLimit()
