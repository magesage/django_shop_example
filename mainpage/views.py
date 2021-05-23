from django.shortcuts import render
from news.models import News


# Create your views here.
def index(request):
    news = News.objects.order_by('-created_at').filter(is_published=True)[0:3]
    return render(request, 'mainpage/index.html', context={'news': news})