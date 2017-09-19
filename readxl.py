import xlrd
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")

# data = xlrd.open_workbook("E:/1work/test.xls")
# table = data.sheets()[0]
# nrows = table.nrows #行数
# ncols = table.ncols #列数
# for i in range(0,nrows):
#     rowValues= table.row_values(i) #某一行数据
#     if rowValues[3]:
#         print(rowValues, type(rowValues))


# from main.models import User
# print(User.objects.all())


def generator():
    for i in range(6):
        yield i**2


b = generator()
for i in b:
    print(i)

print(type(b))