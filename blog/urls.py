# coding:utf8
from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    url(r'^blog_homepage/$', views.blog_homepage, name="blog_homepage"),
    # url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
    url(r'^home/$', views.home, name='home'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^leave_message/$', views.leave_message, name='leave_message'),
    url(r'^about/$', views.about, name='about'),
    url(r'^words/$', views.words, name='words'),
    url(r'^home_leave_message/$', views.home_leave_message, name='home_leave_message'),
    url(r'^album/$', views.album, name='album'),

    url(r'^article_category/$', views.article_category, name='article_category'),
    url(r'^rename_article_column/$', views.rename_article_column, name='rename_article_column'),
    url(r'^del_article_column/$', views.del_article_column, name='del_article_column'),
    url(r'^article_post/$', views.article_post, name='article_post'),
]
