from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'bobshow.views.search', name='search'),
    url(r'^(?P<pk>\d+)/$', 'bobshow.views.detail', name='detail'),
    url(r'^new/$', 'bobshow.views.new', name='new'),
    url(r'^billboard/$', 'bobshow.views.billboard', name='billboard'),
    url(r'^(?P<pk>\d+)/comment_new/$', 'bobshow.views.comment_new', name='comment_new'),
    url(r'^(?P<pk>\d+)/photo_new/$', 'bobshow.views.photo_new', name='photo_new'),
]
