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
  f = open("addfilms/static/addfilms/title.akas.tsv")

  line = f.readline()
  line = f.readline()

  f.close()
  return HttpResponse("{}".format(line))


#def index(request):
  #return HttpResponse("kiedys to moze bedzie baza filmow :)")
