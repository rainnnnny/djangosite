import xlrd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")

import django
django.setup()
from main.models import Express
import django.utils.timezone as timezone
import random
import re



b = list(range(1, 101))
counter = 0
c = []
curMax = 100
while len(b) > 1:
    d = 0
    while d < 7:
        counter += 1
        if counter > curMax:
            counter = counter - curMax
        if counter not in c:
            d += 1
    
    c.append(counter)
    b.remove(counter)
    curMax = max(b)

print(c, b)
for i in range(1, 101):
    if i not in c:
        print(i)