from django.db import models

class Ticket(models.Model):
    tno = models.IntegerField(null=False)
    seat_no = models.IntegerField(null=True)
    cno = models.IntegerField(null=True)
    sno = models.IntegerField(null=False)
    t_state = models.IntegerField(default=1, null=True)

    class Meta:
        db_table = 'ticket'
        unique_together = (('tno', 'sno'),)  # 设置tno和sno的组合为主键
        indexes = [
            models.Index(fields=['cno'], name='cno_index'),
            models.Index(fields=['sno'], name='sno_index'),
        ]
