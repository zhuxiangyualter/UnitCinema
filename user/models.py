from django.db import models

class User(models.Model):
    cno = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, null=True, unique=True)
    user_pass = models.CharField(max_length=30)
    user_real_name = models.CharField(max_length=30)
    user_sex = models.IntegerField(default=1, null=True)
    user_age = models.IntegerField(null=True)
    user_nick_name = models.CharField(max_length=30)
    user_mail = models.CharField(max_length=30, null=True)
    user_reg_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user'
