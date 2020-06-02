import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import loader
from .forms import LoginFrom
from .models import Movie, Genere


def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(username=cd['username'],
                          password=cd['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse('Uwierzytelnienie zakonczone sukcesem.')
        else:
          return HttpResponse('Konto zablokowane.')
      else:
        return HttpResponse('Nieprawidlowe daneuwierzytelniajace')
  else:
    form = LoginForm()
  return render(request, 'addfilms/login.html', {'form': form})


def filldb(request):
  f = open("addfilms/static/addfilms/movies.csv", encoding="utf8")
  f2 = f.read()
  lines = f2.split('\n')

  base = []
  nr = 1
  for line in lines[1:]:
    if nr == (len(lines)-2):
      break

    x = line.split(',')

    film = []
    #film.append(nr)
    if len(x) > 3:
      x2 = x[1] + ', The'
      x2 = x2.strip('"')
      x3 = x[2].split(' (')
      x4 = x3[-1].strip(')"')
      film.append(x2)
      film.append(x4)
    elif len(x) > 2:
      x2 = x[1].split(' (')
      x3 = x2[0]
      x4 = x2[-1].strip(')')
      film.append(x3)
      film.append(x4)

    film.append(x[-1])
    base.append(film)
    print(film)
    #nr+=1

  f.close()

  for film_to_base in base:
    m_serch = Movie.objects.filter(title=film_to_base[0], year=film_to_base[1], gener=film_to_base[2])
    if len(m_serch) > 0:
      continue
    else:
      m = Movie(title=film_to_base[0], year=film_to_base[1], gener=film_to_base[2])
      m.save()

  return HttpResponse("{}".format(base))


#def index(request):
  #return HttpResponse("kiedys to moze bedzie baza filmow :)")


def filldb2(request):
  baza_filmow = Movie.objects.all()

  template = loader.get_template('addfilms/baza_filmow.html')
  context = {
    'baza_filmow': baza_filmow,
  }

  return HttpResponse(template.render(context, request))


def filldb3(request):
  katalogi = os.listdir('addfilms/static/addfilms/movies')
  for k in katalogi:
    filmy = os.listdir('addfilms/static/addfilms/movies/{}'.format(k))
    #print(filmy)
    for film in filmy:
      f = open("addfilms/static/addfilms/movies/{}/{}".format(k,film))
      #print("addfilms/static/addfilms/movies/{}/{}".format(k,film))
      m = json.load(f)
      print(m)

      generes = []
      if 'genre' in m:
        for g in m['genre']:
          g = g.lower().strip()
          g_serch = Genere.objects.filter(name=g)
          if len(g_serch) > 0:
            for gg in g_serch:
              generes.append(gg)
            continue
          else:
            g_add = Genere(name=g)
            g_add.save()
            generes.append(g_add)

      if 'categories' in m:
        for c in m['categories']:
          c = c.lower().strip()
          c_serch = Genere.objects.filter(name=c)
          if len(c_serch) > 0:
            for cc in c_serch:
              generes.append(cc)
            continue
          else:
            c_add = Genere(name=c)
            c_add.save()
            generes.append(c_add)

      print(generes)

      m_serch = Movie.objects.filter(title=m['name'], year=m['year'], director=m['director'])
      if len(m_serch) > 0:
        for g_ in generes:
          m_serch[0].generes.add(g_)
        continue
      else:
        m_add = Movie(title=m['name'], year=m['year'], director=m['director'])
        for g_ in generes:
          m_add.generes.add(g_)
        m_add.save()


      #print(m)
      ### name / year / runtime / categories / relese-date / director / storyline
      f.close()

  return HttpResponse("Films added..")
