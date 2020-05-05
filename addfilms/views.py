import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginFrom
from .models import Movie

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
  baza_filmow = []
  katalogi = os.listdir('addfilms\\static\\addfilms\\movies')
  for k in katalogi:
    filmy = os.listdir('addfilms\\static\\addfilms\\movies\\{}'.format(k))
    print(filmy)
    for film in filmy:
      f = open("addfilms\\static\\addfilms\\movies\\{}\\{}".format(k,film))
      m = json.load(f)
      ### name / year / runtime / categories / relese-date / director / storyline
      baza_filmow.append(m['name'])
      f.close()

  return HttpResponse("Baza zawiera filmy: {}".format(baza_filmow))
