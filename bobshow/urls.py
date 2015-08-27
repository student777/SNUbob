from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'bobshow.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'bobshow.views.detail', name='detail'),
    url(r'^new/$', 'bobshow.views.new', name='new'),
    url(r'^(?P<pk>\d+)/comment_new/$', 'bobshow.views.comment_new', name='comment_new'),
]

