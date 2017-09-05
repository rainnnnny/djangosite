from django.db import models


class User(models.Model):
    Account = models.CharField(max_length=15)
    Password = models.CharField(max_length=16)

    def __str__(self):
        return self.Account

    def PswVerify(self, sPsw):
        return sPsw == self.Password
