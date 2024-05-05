from django.db import models
from rest_framework import serializers

from user.models import User


class Notice(models.Model):
    nno = models.AutoField(primary_key=True)
    wno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    ncontent = models.TextField(null=True)
    re_date = models.DateTimeField(null=True, auto_now_add=True)
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['nno', 'title', 'ncontent', 're_date']
        read_only_fields = ['nno', 're_date']