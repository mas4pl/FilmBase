from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginFrom

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
  f = open("addfilms/static/addfilms/movies.csv", encoding="utf8").read()
  lines = f.split('\n')

  base = []
  nr = 1
for line in lines[1:]:
  if nr == (len(lines)-2):
    break

  x = line.split(',')

  film = []
  film.append(nr)
    if len(x) > 3:
      x2 = x[1] + ', The'
      film.append(x2)
    else:
      x2 =str(x[1])
      for i in x2[-1:-7]:
        x2.remove(x2[i])
      film.append(x2)

    film.append(x[-1])
    base.append(film)
    print(film)
    nr+=1

  f.close()
  return HttpResponse("{}".format(base))


#def index(request):
  #return HttpResponse("kiedys to moze bedzie baza filmow :)")
