#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from django import forms

class TestForm(forms.Form):
    Acc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"账号或手机"}), label="", max_length=10)
    Psw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"密码"}), label="", max_length=30)


def index(request):
    sResult = ""

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            Acc = request.POST['Acc']
            Psw = request.POST['Psw']
            if Acc == "test" and Psw == "2333":
                return HttpResponseRedirect('/test/hello/')
            else:
                sResult = "account or password error"

    else:
        form = TestForm()

    return render(request, "login1.html", {'form':form, 'sResult':sResult})

def hello(request):
    return render(request, "index1.html")

def ajax_list(request):
    a = list(range(100))
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    name_dict = {'pyt': 'life is short, ', 'hon': 'I use __'}
    return JsonResponse(name_dict)


def test(request):
    sTest = "asdf123花生豆腐"
    lList = ["HTML", "CSS", "javaScript", "Python", "Django"]
    dDict = {'a':1, 'b':2, 'c':3}
    iTest = request.GET.get('iTest')
    return render(request, 'test.html', {'sTest':sTest, 'lList':lList, 'dDict':dDict, 'iTest':iTest})


def add(request):
    a = request.POST['a']
    b = request.POST['b']
    c = int(a) * int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
