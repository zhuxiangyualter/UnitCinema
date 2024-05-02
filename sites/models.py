from django.db import models

class site(models.Model):
    sno = models.AutoField(primary_key=True)
    hno = models.IntegerField(null=True)
    begintime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    fno = models.IntegerField(null=True)
    wno = models.IntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['fno'], name='fno_index'),
            models.Index(fields=['hno'], name='hno_index'),
            models.Index(fields=['wno'], name='wno_index'),
        ]
        db_table = 'sites'