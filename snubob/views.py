from django.shortcuts import render
from bobshow.models import Bob, Comment

def index(request):
    return render(request, "index.html", {
        })
