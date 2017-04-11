from django.shortcuts import render, get_object_or_404, redirect
from bobshow.models import Bob, Date
from bobshow.forms import CommentForm, ImageForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def index(request):
    today = Date.objects.get(time=datetime.date.today())
    bob_list = Bob.objects.filter(date=today).order_by('place')
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
    comment_form = CommentForm(auto_id=False)
    return render(request, "detail.html", {'bob': bob, 'comment_form': comment_form, })


def billboard(request):
    bob_list = Bob.objects.order_by('-score')[:10]
    return render(request, "billboard.html", {'bob_list': bob_list, })


def comment_new(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.is_ajax():
                comment = form.save(commit=False)
                comment.bob = bob
                comment.star = request.POST['star']
                comment.save()
                bob.cal_mean()
                return render(request, 'comment_row.html', {'comment': comment})
    return redirect('bobshow:detail', pk)


def add_image(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.bob = bob
            image.save()
            return redirect('bobshow:detail', pk)
    else:
        form = ImageForm()
    return render(request, 'form.html', {'form': form})
