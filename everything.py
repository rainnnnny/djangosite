import xlrd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句

否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
import django
django.setup()
from main.models import Express
import django.utils.timezone as timezone
import random
import re

all = Express.objects.all().values()
for each in all:
    sid = each['shelfID']
    if not re.match("[a-z][0-9]{4}", sid):
        a  = random.randint(97, 122)
        c = chr(a)
        b = random.randint(1000, 9999)
        s = "%s%s"%(c,b)
        o = Express.objects.get(id=each['id'])
        o.shelfID=s
        o.save()
        print(s)
