from django.shortcuts import render, get_object_or_404, redirect
from bobshow.models import Bob, Date, Image, Place, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
import datetime


def index(request):
    today = Date.objects.get(time=datetime.date.today())
    bob_list = []
    for place in Place.objects.all():
        bobs = Bob.objects.filter(date=today, place=place)
        bob_list.append((bobs, place))

    return render(request, "index.html", {'bob_list': bob_list, 'today': today, })


def search(request):
    name = request.GET.get('name', "")
    bob_list = Bob.objects.filter(name__contains=name)
    paginator = Paginator(bob_list, 32)
    page = request.GET.get('page')

    try:
        bob_paginated = paginator.page(page)
    except PageNotAnInteger:
        bob_paginated = paginator.page(1)
    except EmptyPage:
        bob_paginated = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'bob_list': bob_paginated, 'name': name})


def detail(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    return render(request, "detail.html", {'bob': bob})


def billboard(request):
    bob_list = Bob.objects.order_by('-score')[:10]
    return render(request, "billboard.html", {'bob_list': bob_list, })


def comment_new(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    if request.method == 'POST':
        if request.is_ajax():
            content = request.POST['content']
            star = request.POST['star']
            comment = Comment.objects.create(content=content, star=star, bob=bob)
            bob.cal_mean()
            return render(request, 'comment_row.html', {'comment': comment})


def add_image(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    if request.method == 'POST':
        image = request.FILES['image']
        img = Image(image=image, bob=bob)
        img.save()  # Image.objects.create raises an Integerity error...?
        return HttpResponse(status=201)
