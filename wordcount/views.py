from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    context = {}
    context['name'] = "HASEEB"
    return render(request, "home.html",context)

def count(request):
    fulltext = request.GET['fulltext']
    context = {}
    wordlist = fulltext.split()
    context['fulltext'] = fulltext
    context['count'] = len(wordlist)
    
    worddict = {}
    for word in wordlist :
        if word in worddict:
            worddict[word] +=1
        else :
            worddict[word] = 1
    context['worddict'] = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, "count.html", context)

def about(request):
    context = {}
    context['descrription'] = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    return render(request, "about.html",context)

    