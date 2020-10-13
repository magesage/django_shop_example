from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    posts = News.objects.all()
    return render(request, 'news/index.html', context={'n': posts})