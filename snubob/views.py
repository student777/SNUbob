from django.shortcuts import render
from bobshow.models import Bob, Date
import datetime


def index(request):
    today = Date.objects.get(time=datetime.date.today())
    bob_list = Bob.objects.filter(date=today).order_by('place')
    return render(request, "index.html", {'bob_list': bob_list, 'today': today, })
