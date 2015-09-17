from django.shortcuts import render
from bobshow.models import Bob
import datetime


def index(request):
    dat = datetime.date.today().isoformat()+'\n'
    bob_list = Bob.objects.filter(content__contains=dat).order_by('place')
    return render(request, "index.html", {'bob_list': bob_list, })
