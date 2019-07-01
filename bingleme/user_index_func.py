from userModel.models import Medicine,ImageMedicine,Order
from django.shortcuts import render

def checkClassification():
    classify=Medicine.objects.raw('select id,classfication from usermodel_medicine group by classfication')
    classes=[]
    for foo in classify:
        classes.append(foo.classfication)
    return classes

def getHeatMedicine():
    result=Order.objects.raw('select id,medicineID_id,sum(number) from usermodel_order group by medicineID_id ORDER BY sum(number) DESC')#后续需要改成推荐
    mid=[]
    for foo in range(0,9):
        mid.append(str(result[foo].medicineID_id))
    result = ImageMedicine.objects.raw(
        'select * from usermodel_imagemedicine where medicineID_id in ('+",".join(mid)+") group by medicineID_id")  # 后续需要改成推荐
    h_medicine1=[]
    h_medicine2=[]
    for foo in result[0:4]:
        info={"generalName":foo.medicineID.generalName,"price":foo.medicineID.price,"url":foo.imageUrl,"medicine_id":foo.medicineID_id}
        h_medicine1.append(info)
    for foo in result[4:8]:
        info = {"generalName": foo.medicineID.generalName, "price": foo.medicineID.price, "url": foo.imageUrl,"medicine_id":foo.medicineID_id}
        h_medicine2.append(info)
    return h_medicine1,h_medicine2




