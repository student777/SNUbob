from django.shortcuts import render
from bobshow.models import Bob


def index(request):
    bob_list = Bob.objects.filter(content__contains='2015-09-14').order_by('place')
    return render(request, "index.html", {'bob_list': bob_list, })
