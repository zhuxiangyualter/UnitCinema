from django.db import models

class Hall(models.Model):
    hno = models.AutoField(primary_key=True)
    hall_name = models.CharField(max_length=50)
    seat_num = models.IntegerField()
    hall_state = models.IntegerField(default=0, null=True)
