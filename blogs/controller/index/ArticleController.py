from django.http import HttpResponse, Http404
from blogs.models import Article
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
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
