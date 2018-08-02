from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^add_evaluation/$', views.add_evaluation, name='add_evaluation'),
    url(r'^recommend/$', views.recommend, name='recommend'),
    url(r'^boxoffice/$', views.boxoffice, name='boxoffice'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

