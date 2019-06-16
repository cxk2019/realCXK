from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  #自增主键
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)
    realname = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=10)
    regtime = models.DateTimeField(default=timezone.now)  # 缺省值是当前时间





