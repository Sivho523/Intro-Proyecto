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
    condicion = condicion.replace(' ','+')
    print(condicion)
    url_medlineplusapi = urllib.request.Request(f'https://wsearch.nlm.nih.gov/ws/query?db=healthTopicsSpanish&term={condicion}')
    source = urllib.request.urlopen(url_medlineplusapi).read()
    obj = xmltodict.parse(source)
    #print(json.dumps(obj))

    #list = obj["nlmSearchResult"]["list"]["document"][0]["content"][6]["#text"]
    #list = list.replace("<p>","").replace('<span class="qt0">',"").replace("</span>","").replace("</p>","")
    #data = { "resumen": list
    #}

    list = obj["nlmSearchResult"]["list"]["document"][0]["content"]
    for dou in list:
        for valor in dou:
            print(dou[valor])
            if dou[valor] == "FullSummary":
                textaco = dou['#text']
                print(textaco)
                #list = obj["nlmSearchResult"]["list"]["document"][0]["content"][dou[str(valor)]]
                #print(list)
                list = textaco
    #print(list)
    list = list.replace("<p>","").replace('<span class="qt0">',"").replace("</span>","").replace("</p>","")
    list = list.replace('<span class="qt1">',"").replace("<ul>","").replace("<li>","").replace("</li>","").replace("</ul>","")
    list = list.replace(' <span class="qt2">',"").replace('<span class="qt3">',"")
    data = { "resumen": list
    }

    return render(request, "resultados.html", data)
    #return render(request, "resultados.html", obj)