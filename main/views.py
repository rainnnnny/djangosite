from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# from django import forms
#
# class AddForm(forms.Form):
#     acc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "账号或手机"}), label='', max_length=30)
#     psw = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "密码"}), label='', max_length=16)
#
def login(request):
    # if request.method == 'POST':# 当提交表单时
    #
    #     form = AddForm(request.POST) # form 包含提交的数据
    #
    #     if form.is_valid():# 如果提交的数据合法
    #         acc = form.cleaned_data['acc']
    #         psw = form.cleaned_data['psw']
    #         iResult = AccVerify(acc, psw)
    #         return HttpResponse(iResult)
    #
    # else:# 当正常访问时
    #     form = AddForm()
    # return render(request, 'login.html', {'form': form})

    if request.method == 'POST':# 当提交表单时
        acc = request.POST['account']
        psw = request.POST['password']
        iResult = AccVerify(acc, psw)
        if iResult == 1:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'iResult':iResult})
    else:
        return render(request, 'login.html')

def AccVerify(acc, psw):
    oQuerySet = User.objects.filter(Account=acc)
    if not oQuerySet:
        return -1
    oUser = oQuerySet[0]
    if not oUser.PswVerify(psw):
        return 0
    return 1
