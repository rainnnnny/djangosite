"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from helloapp import views as helloviews
from main import views as mainviews

urlpatterns = [
	url(r'^test$', helloviews.test, name='test'),
	url(r'^add/$', helloviews.add, name='add'),
	url(r'^add/(\d+)/(\d+)/$', helloviews.old_add2_redirect),
	url(r'^new_add/(\d+)/(\d+)/$', helloviews.add2, name='add2'),

	url(r'^$', mainviews.login, name="login"),
	url(r'^admin/', admin.site.urls),
	url(r'^OnLogin/$', mainviews.OnLogin, name="OnLogin"),

]
