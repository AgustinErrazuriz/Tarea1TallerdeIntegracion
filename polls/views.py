from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    r1 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    r1 = r1.json()
    tempbb = []

    for capitulo in r1:
        tempbb.append(capitulo["season"])
    tempbb = sorted(list(set(tempbb)))

    r2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    r2 = r2.json()
    tempbcs = []
    
    for capitulo in r2:
        tempbcs.append(capitulo["season"])
    tempbcs = sorted(list(set(tempbcs)))

    context = {'tempbb': tempbb,
               'tempbcs': tempbcs}
    
    return render(request, 'polls/index.html', context)

def capitulos(request, serie, temporada):
    if serie == "breakingbad":
        nom = "Breaking Bad"
        r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
        r = r.json()
    else:
        nom = "Better Call Saul"
        r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
        r = r.json()

    cap = []

    for capitulo in r:
        if capitulo["season"] == temporada:
            cap.append(capitulo["title"])

    context = {'cap': cap,
               'serie': serie,
               'temporada': temporada,
               'nom': nom}

    return render(request, 'polls/capitulos.html', context)

def episodio(request, serie, temporada, capitulo):
    if serie == "breakingbad":
        nom = "Breaking Bad"
        r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
        r = r.json()
    else:
        nom = "Better Call Saul"
        r = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
        r = r.json()
    for cap in r:
        if cap["title"] == capitulo:
            context = {'episode_id': cap["episode_id"],
                       'title': cap["title"],
                       'season': cap["season"],
                       'episode': cap["episode"],
                       'air_date': cap["air_date"],
                       'characters': cap["characters"],
                       'serie': nom}

    return render(request, 'polls/episodio.html', context)

def personaje(request, nombre):
    nom = nombre
    nom = nom.replace(" ", "+")
    gg = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={}'.format(nom)
    r = requests.get(gg)
    r = r.json()
    for per in r:
        if per["name"] == nombre:
            context = {'char_id': per["char_id"],
                       'name': nombre,
                       'occupation': per["occupation"],
                       'img': per["img"],
                       'status': per["status"],
                       'appearance': per["appearance"],
                       'nickname': per["nickname"],
                       'portrayed': per["portrayed"],
                       'category': per["category"],
                       'better_call_saul_appearance': per["better_call_saul_appearance"]}

    hh = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={}'.format(nom)
    r2 = requests.get(hh)
    r2 = r2.json()
    quotes = []
    for q in r2:
        quotes.append(q["quote"])
    context['quotes'] = quotes
    
    return render(request, 'polls/personaje.html', context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        search = search.rstrip()
        search = search.replace(" ", "+")
        res = []
        if search is not '':
            gg = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={}'.format(search)
            r = requests.get(gg)
            r = r.json()
            for q in r:
                res.append(q["name"])
        context = {'nombres': res}

        return render(request, 'polls/search.html', context)
