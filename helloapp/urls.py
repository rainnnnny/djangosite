
from django.conf.urls import url
from helloapp import views as helloviews

from django.views.generic import TemplateView

urlpatterns = [
	url(r'^index/$', helloviews.index, name='index1'),
	url(r'^hello/$', helloviews.hello, name='hello'),
	url(r'^test/$', helloviews.test, name='test'),
	url(r'^add/$', helloviews.add, name='add'),
	url(r'^add/(\d+)/(\d+)/$', helloviews.old_add2_redirect),
	url(r'^new_add/(\d+)/(\d+)/$', helloviews.add2, name='add2'),
	url(r'^ajax_list/$', helloviews.ajax_list, name='ajax_list'),
	url(r'^ajax_dict/$', helloviews.ajax_dict, name='ajax_dict'),
]
