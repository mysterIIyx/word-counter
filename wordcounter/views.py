from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hitere':'This is me'})

def gallery(request):
        return render(request, 'gallery.html')

def kontakt(request):
        return render(request, 'kontakt.html')

def about(request):
        return render(request, 'about.html')

def warto(request):
        return render(request, 'warto.html')

def count(request):

        fulltext = request.GET['fulltext']
        wordlist = fulltext.split()
        print(len(wordlist))
        return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist)})


def grz(request):
        return HttpResponse('hello grz')
