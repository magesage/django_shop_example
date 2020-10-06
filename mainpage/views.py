from django.shortcuts import render

# Create your views here.
def index(request):
    n = ['Oleg', 'Masha', 'Olja', 'Ksu']
    return render(request, 'mainpage/index.html', context={'names': n})