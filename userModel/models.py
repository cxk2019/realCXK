from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)
    realname = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    regtime = models.DateTimeField(default=timezone.now)  # 缺省值是当前时间

class Medicine(models.Model):
    price = models.CharField(max_length=10)
    general_name = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    goods_name = models.CharField(max_length=30)
    component = models.CharField(max_length=200)
    character = models.CharField(max_length=300)
    function = models.CharField(max_length=300)
    specification = models.CharField(max_length=100)
    usageAndDosage = models.CharField(max_length=300)
    adverseReaction = models.CharField(max_length=2000)
    contraindication = models.CharField(max_length=200)
    attention = models.CharField(max_length=1000)
    drugInteraction = models.CharField(max_length=1000)
    storage = models.CharField(max_length=200)
    packing = models.CharField(max_length=100)
    termOfValidity = models.CharField(max_length=20)
    approvalNumber = models.CharField(max_length=30)
    enterpriseName = models.CharField(max_length=50)

class Order():
    place_time = models.DateTimeField(default=timezone.now)
    medicine_id = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    number = models.IntegerField(max_length=10)
    state = models.CharField(max_length=10)
    pay_mode = models.CharField(max_length=20)
    dis_mode = models.CharField(max_length=20)
    user_id = models.ForeignKey('User')
    # user_id = models.ForeignKey('User',on_delete=models.CASCADE)
    del_time = models.DateTimeField(default=timezone.now)
    rec_time = models.DateTimeField(default=timezone.now)
    acc_time = models.DateTimeField(default=timezone.now)

class ImageMedicine(models.Model):
    imageUrl=models.CharField(max_length=60)
    medicineID=models.ForeignKey('Medicine')

class Cart(models.Model):
    user = models.ForeignKey('User')
    medicine = models.ForeignKey('Medicine')
    number = models.IntegerField()
