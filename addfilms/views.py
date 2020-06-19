import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import loader
from .forms import LoginFrom
from .models import Movie, Genere

def home(request):
  baza_filmow_rob = Movie.objects.all()
  if len(baza_filmow_rob) <= 5:
      last_films = baza_filmow_rob
  else:
      last_films = baza_filmow_rob[len(baza_filmow_rob)-5:]
  template = loader.get_template('addfilms/strona_startowa.html')
  context = {
    'last_films': last_films,
  }

  return HttpResponse(template.render(context, request))


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
        return HttpResponse('Nieprawidlowe dane uwierzytelniajace')
  else:
    form = LoginFrom()
  return render(request, 'addfilms/login.html', {'form': form})


def user_aut(request):
  if request.user.is_authenticated:
    # Do something for authenticated users.
    status = 'zalogowano'
  else:
    # Do something for anonymous users.
    status = 'nie zalogowano'

  """
  username = request.POST.get('username', False)
  password = request.POST.get('password', False)
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirect to a success page.
    status = 'zalogowano'
  else:
    # Return an 'invalid login' error message.
    status = 'nie_zalogowano'
  """
  print(status)
  return HttpResponse("{}".format(status))

def add_user_films():
    baza_filmow = Movie.objects.all()
    

    return HttpResponse

def user_last_films(request):
    baza_filmow_rob = Movie.objects.filter(users=user)
    if len(baza_filmow_rob) <= 5:
        user_last_films = baza_filmow_rob
    else:
        user_last_films = baza_filmow_rob[len(baza_filmow_rob)-5:]
    template = loader.get_template('addfilms/user_profil.html')
    context = {
      'last_films': last_films,
    }

    return HttpResponse(template.render(context, request))


def view_all(request):
  baza_filmow = Movie.objects.all()
  template = loader.get_template('addfilms/baza_filmow.html')
  context = {
    'baza_filmow': baza_filmow,
  }

  return HttpResponse(template.render(context, request))


def filldb(request):
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
