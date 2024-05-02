from django.db import models

class Film(models.Model):
    fno = models.AutoField(primary_key=True)
    film_name = models.CharField(max_length=50, null=False)
    director = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    duration = models.FloatField(default=0, null=True)
    uptime = models.DateField(null=True, blank=True)
    downtime = models.DateField(null=True, blank=True)
    price = models.FloatField(default=0, null=True)
    avg_grade = models.FloatField(default=0, null=True)
    intro = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'film'  # 指定数据库中的表名
