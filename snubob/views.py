from django.shortcuts import render
from bobshow.models import Bob
import datetime
from datetime import timedelta


def index(request):
    dt = datetime.datetime.now() + timedelta(hours=9)
    dat = dt.date().isoformat()+'\n'
    bob_list = Bob.objects.filter(content__contains=dat).order_by('place')
    return render(request, "index.html", {'bob_list': bob_list, 'today': dat, })
