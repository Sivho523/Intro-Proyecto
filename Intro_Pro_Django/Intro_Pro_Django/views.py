from django.shortcuts import render

def index (request):
    return render(request,"index.html")

def wikisearch (request):
    return render(request,"wikisearch.html")

def login (request):
    return render(request,"login.html")

def register (request):
    return render(request,"register.html")

def xml (request):
    return render(request, "trivia.html")