from django.db import models
from rest_framework import serializers
class Evaluate(models.Model):
    cno = models.IntegerField(null=False)
    fno = models.IntegerField(null=False)
    grade = models.IntegerField(null=True, blank=True)  # 允许空值且在表单中可以不填
    econtent = models.CharField(max_length=300, null=True, blank=True)
    eva_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'evaluate'  # 指定数据库中的表名
        unique_together = (('cno', 'fno'),)  # 设置cno和fno的组合为唯一约束
        indexes = [
            models.Index(fields=['fno'], name='fno_index')
        ]
class EvaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluate
        fields = [
            'fno',
            'cno',
            'grade',
            'econtent',
            'eva_date'
        ]
        read_only_fields = ['fno','cno']