from django.db import models

class Worker(models.Model):
    wno = models.AutoField(primary_key=True)
    work_real_name = models.CharField(max_length=30)
    work_sex = models.IntegerField(default=1, null=True)
    work_age = models.IntegerField(null=True)
    work_name = models.CharField(max_length=50, null=True, unique=True)
    work_pass = models.CharField(max_length=30)
    work_nick_name = models.CharField(max_length=30)
    work_mail = models.CharField(max_length=30)
    work_reg_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'worker'
