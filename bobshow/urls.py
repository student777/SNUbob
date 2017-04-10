from django.conf.urls import url
from bobshow import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^billboard/$', views.billboard, name='billboard'),
    url(r'^(?P<pk>\d+)/comment_new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<pk>\d+)/add_image/$', views.add_image, name='image_new'),
]
