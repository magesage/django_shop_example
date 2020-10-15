from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator


# Create your views here.
def news_list(request):
    news = News.objects.order_by('-created_at').filter(is_published=True)
    paginator = Paginator(news, 5)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/index.html', context={'page_obj': page_objects})


def news_article(request, slug):
    article = News.objects.get(slug__iexact=slug)
    return render(request, 'news/article.html', context={'page_obj': article})
