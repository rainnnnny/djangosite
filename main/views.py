import math

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User, Express, Express_delivery
from hellodjango.defines import *

# from django import forms
#
# class AddForm(forms.Form):
#     acc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "账号或手机"}), label='', max_length=30)
#     psw = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "密码"}), label='', max_length=16)
#
# def login(request):
    # if request.method == 'POST':# 当提交表单时
    #
    #     form = AddForm(request.POST) # form 包含提交的数据
    #
    #     if form.is_valid():# 如果提交的数据合法
    #         acc = form.cleaned_data['acc']
    #         psw = form.cleaned_data['psw']
    #         iResult = Authenticate(acc, psw)
    #         return HttpResponse(iResult)
    #
    # else:# 当正常访问时
    #     form = AddForm()
    # return render(request, 'login.html', {'form': form})

def index(request):
    user = request.session.get('id_logged_in') or request.COOKIES.get('id_logged_in')
    if user:
        return render(request, 'index.html', {'user':user})

    if request.method == 'POST':# 当提交表单时
        acc = request.POST['account']
        psw = request.POST['password']
        bRemember = request.POST.getlist('remember')
        iResult = Authenticate(acc, psw)
        if iResult == AUTH_SUCCESS:
            if bRemember:
                request.session['id_logged_in'] = acc
            response = redirect('/index/')
            response.set_cookie("id_logged_in", acc)#, secure=True)
            return response
        else:
            return render(request, 'login.html', {'sResult':AUTH_MSG[iResult]})
            # return HttpResponse(AUTH_MSG[iResult])
    else:
        return render(request, 'login.html')

def logout(request):
    try:
        del request.session['id_logged_in']
    except KeyError:
        pass
    response = redirect('/index/')
    response.delete_cookie('id_logged_in')
    return response

def Authenticate(acc, psw):
    oQuerySet = User.objects.filter(Account=acc)
    if not oQuerySet:
        return AUTH_ACCERROR
    oUser = oQuerySet[0]
    if not oUser.PswVerify(psw):
        return AUTH_PSWERROR
    return AUTH_SUCCESS

# AUTH END


def express(request, iPage):
    iPage = int(iPage)
    oQuerySet = Express.objects.all()
    lData = oQuerySet.values()
    data = []
    for dData in lData:
        dData.pop('id')
        data.append(dData)
    iLen = len(data)
    iPageCount = math.ceil(len(data) / EXPRESS_PAGE_ITEM_NUM)
    start = iPage*EXPRESS_PAGE_ITEM_NUM
    data = data[start:(start+EXPRESS_PAGE_ITEM_NUM)]
    return render(request, 'express.html', {'lData':data, 'iPageCount':iPageCount, 'oRange':range(iPageCount), 'iPage':iPage})
