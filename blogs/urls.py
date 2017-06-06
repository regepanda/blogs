from django.conf.urls import url
from controller import ArticleController

urlpatterns = [
    # ex: /blogs/
    url(r'^$', ArticleController.index, name='index'),
    # ex: /blogs/5/
    url(r'^(?P<article_id>[0-9]+)/$', ArticleController.detail, name='detail'),
    # ex: /blogs/5/update/
    url(r'^(?P<article_id>[0-9]+)/update/$', ArticleController.update, name='update'),
    # ex: /blogs/5/delete/
    url(r'^(?P<article_id>[0-9]+)/delete/$', ArticleController.delete, name='delete'),
]