from django.shortcuts import render
import xmltodict, json
import urllib

def index (request):
    return render(request,"index.html")

def wikisearch (request):
    return render(request,"wikisearch.html")

def login (request):
    return render(request,"login.html")

def register (request):
    return render(request,"register.html")

def trivia (request):
    return render(request, "trivia.html")

def xml (request):
    condicion = request.POST['sickness']
    condicion = condicion.replace(' ', '+')
    url_medlineplusapi = urllib.request.Request(f'https://wsearch.nlm.nih.gov/ws/query?db=healthTopicsSpanish&term={condicion}')
    source = urllib.request.urlopen(url_medlineplusapi).read()
    obj = xmltodict.parse(source)
    print(json.dumps(obj))