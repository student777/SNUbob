from django.conf.urls import url
from bobshow import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^billboard/$', views.billboard, name='billboard'),
    url(r'^(?P<pk>\d+)/comment_new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<pk>\d+)/photo_new/$', views.photo_new, name='photo_new'),
]
