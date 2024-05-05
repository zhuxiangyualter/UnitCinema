from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
class User(models.Model):
    cno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=30)
    user_real_name = models.CharField(max_length=30)
    user_sex = models.IntegerField(default=1, null=True)
    user_age = models.IntegerField(null=True)
    user_nick_name = models.CharField(max_length=30)
    user_mail = models.CharField(max_length=30, null=True)
    user_reg_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user