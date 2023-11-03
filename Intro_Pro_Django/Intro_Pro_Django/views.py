from django.shortcuts import render

def index (request):
    return render(request,"index.html")

def wikisearch (request):
    return render(request,"wikisearch.html")