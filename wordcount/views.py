from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def countpage(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist)})
