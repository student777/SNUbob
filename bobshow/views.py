from django.shortcuts import render, get_object_or_404, redirect
from bobshow.models import Bob, Comment
from django.contrib.auth.models import User
from django.contrib import messages
from bobshow.forms import BobForm, CommentForm
from django.http import Http404, HttpResponse


def index(request):
    if request.GET.get('name'):
        name = request.GET.get('name')
        bob_list = Bob.objects.filter(name__startswith=name)
    else:
        bob_list = Bob.objects.all()
    return render(request, "bobshow/index.html", {
        'bob_list': bob_list,
        })


def detail(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    comment_form = CommentForm(auto_id=False)
    return render(request, "bobshow/detail.html", {
        'bob': bob, 'comment_form': comment_form,
        })


def new(request):
    if request.method == 'POST':
        form = BobForm(request.POST, request.FILES)
        if form.is_valid():
            bob = form.save(commit=False)
            if request.user.is_authenticated():
                bob.author = request.user
            else:
                bob.author = User.objects.get(username='noname')
            bob.score = bob.star
            bob.save()
            messages.success(request, "새 글이 등록되었습니다")
            return redirect('bobshow:index')
    else:
        form = BobForm()
    return render(request, 'form.html', {
        'form': form, 'title': 'New Post'})


def comment_new(request, pk):
    bob = get_object_or_404(Bob, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.is_ajax():
                comment = form.save(commit=False)
                comment.bob = bob
                if request.user.is_authenticated():
                    comment.author = request.user
                else:
                    comment.author = User.objects.get(username='noname')
                comment.star = request.POST['star']
                comment.save()
                bob.cal_mean()
                return render(request, 'bobshow/comment_row.html', {
                    'comment': comment,
                })
    return redirect('bobshow:detail', pk)
