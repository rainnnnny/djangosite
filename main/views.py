from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def AccVerify(acc, psw):
	oUser = User.objects.filter(Account=acc)
	if not oUser:
		return -1
	if not oUser.PswVerify(psw):
		return 0
	return 1

def login(request):
	return render(request, 'login.html')

def OnLogin(request):
	acc = request.POST['account']
	psw = request.POST['password']
	iResult = AccVerify(acc, psw)

	return HttpResponse(iResult)
