from django.http import HttpResponse
from ..models import Article
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
    return HttpResponse("article detail with article_id:" + article_id)


def update(request, article_id=0):
    return HttpResponse("article update with article_id:" + article_id)


def delete(request, article_id=0):
    return HttpResponse("article delete with article_id:" + article_id)
