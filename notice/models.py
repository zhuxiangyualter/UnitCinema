from django.db import models

class Notice(models.Model):
    nno = models.AutoField(primary_key=True)
    wno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    ncontent = models.TextField(null=True)
    re_date = models.DateTimeField(null=True)
