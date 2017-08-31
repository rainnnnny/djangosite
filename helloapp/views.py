#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
	sTest = "asdf123花生豆腐"
	lList = ["HTML", "CSS", "javaScript", "Python", "Django"]
	dDict = {'a':1, 'b':2, 'c':3}
	return render(request, 'home.html', {'sTest':sTest, 'lList':lList, 'dDict':dDict})

def hello(request):
	return HttpResponse("Hello django! ")

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(
		reverse('add2', args=(a, b))
	)
