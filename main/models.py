from django.db import models

class User(models.Model):
    Account = models.CharField(max_length=15)
    Password = models.CharField(max_length=16)

    def __str__(self):
        return self.Account

    def PswVerify(self, sPsw):
        return sPsw == self.Password


class Express(models.Model):
    express_number = models.BigIntegerField()
    express_company = models.CharField(max_length=10)
    shelfID = models.CharField(max_length=5)
    recipient = models.CharField(max_length=5)
    recipient_phone = models.BigIntegerField()
    address = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    leave_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=10) #未取件,已取件,问题件,拒收,无人领取,其他

    def __str__(self):
        return self.recipient

class Express_delivery(models.Model):
    express_number = models.BigIntegerField()
    express_company = models.CharField(max_length=10)
    shelfID = models.CharField(max_length=5)
    recipient = models.CharField(max_length=5)
    recipient_phone = models.BigIntegerField()
    address = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    leave_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=10) #未揽件,已揽件,已发出,其他
    sender = models.CharField(max_length=5)
    sender_phone = models.BigIntegerField()

    def __str__(self):
        return self.recipient
