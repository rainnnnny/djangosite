from django.db import models

class User(models.Model):
    Account = models.CharField(max_length=15)
    Password = models.CharField(max_length=16)

    def __str__(self):
        return self.Account

    def PswVerify(self, sPsw):
        return sPsw == self.Password


class Express(models.Model):
    STATUS = (
        ('0', '未取件'),
        ('1', '已取件'),
        ('2', '问题件'),
        ('3', '拒收'),
        ('4', '无人领取'),
        ('5', '其他'),
    )
    express_number = models.BigIntegerField()
    express_company = models.CharField(max_length=10)
    shelfID = models.CharField(max_length=5)
    recipient = models.CharField(max_length=5)
    recipient_phone = models.BigIntegerField()
    address = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    leave_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS) #未取件,已取件,问题件,拒收,无人领取,其他

    def __str__(self):
        return self.recipient

class Express_delivery(models.Model):
    STATUS = (
        ('0', '未揽件'),
        ('1', '已揽件'),
        ('2', '已发出'),
        ('3', '其他'),
    )
    express_number = models.BigIntegerField()
    express_company = models.CharField(max_length=10)
    shelfID = models.CharField(max_length=5)
    recipient = models.CharField(max_length=5)
    recipient_phone = models.BigIntegerField()
    address = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    leave_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, choices=STATUS) #未揽件,已揽件,已发出,其他
    sender = models.CharField(max_length=5)
    sender_phone = models.BigIntegerField()

    def __str__(self):
        return self.recipient
