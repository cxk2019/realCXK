from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=60)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)
    realName = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=10)
    regtime = models.DateTimeField(default=timezone.now)  # 缺省值是当前时间

class Medicine(models.Model):
    price = models.CharField(max_length=10)
    generalName = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    goodsName = models.CharField(max_length=30)
    component = models.CharField(max_length=200)
    character = models.CharField(max_length=300)
    function = models.CharField(max_length=300)
    specification = models.CharField(max_length=100)
    usageAndDosage = models.CharField(max_length=1000)
    adverseReaction = models.CharField(max_length=2000)
    contraindication = models.CharField(max_length=1000)
    attention = models.CharField(max_length=1000)
    drugInteraction = models.CharField(max_length=1000)
    storage = models.CharField(max_length=200)
    packing = models.CharField(max_length=100)
    termOfValidity = models.CharField(max_length=100)
    approvalNumber = models.CharField(max_length=100)
    enterpriseName = models.CharField(max_length=100)
    category = models.IntegerField()

class Order(models.Model):
    placeTime = models.DateTimeField(default=timezone.now)
    medicineID = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    number = models.IntegerField()
    state = models.CharField(max_length=10)
    payMode = models.CharField(max_length=20)
    disMode = models.CharField(max_length=20)
    userID = models.ForeignKey('User',on_delete=models.CASCADE)
    delTime = models.DateTimeField(default=timezone.now)
    recTime = models.DateTimeField(default=timezone.now)
    accTime = models.DateTimeField(default=timezone.now)

class ImageMedicine(models.Model):
    imageUrl=models.CharField(max_length=60)
    medicineID=models.ForeignKey('Medicine',on_delete=models.CASCADE)

class Cart(models.Model):
    userID = models.ForeignKey('User',on_delete=models.CASCADE)
    medicineID = models.ForeignKey('Medicine',on_delete=models.CASCADE)
    number = models.IntegerField()
