from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from .models import News


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'main.html', {'username': username, 'errors': True})
    raise Http404


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/")



def main_page(request):
	return render(request, 'main.html')

def contacts(request):
	return render(request, 'contacts.html')

def galary(request):
	return render(request, 'galary.html')

def menu(request):
	return render(request, 'menu.html')

def news(request):
	news = News.objects.all()
	return render(request, 'news.html', {'news':news})

def reviews(request):
	return render(request, 'reviews.html')

def stakes(request):
	return render(request, 'stakes.html')