from userModel.models import Medicine,ImageMedicine,User,Order,RealOrder
from django.shortcuts import render
import datetime

def orderInfo(id):#从历史订单跳过来
    o=Order.objects.raw('select * from usermodel_order where  id = ' + str(id))
    return o[0].realOrderID_id

def checkOrder(id):
    o=Order.objects.raw('select * from usermodel_order where realOrderID_id = "'+ str(id) +'"')
    print(o.__len__())
    info={"id":id,"time":o[0].realOrderID.placeTime,"payMode":o[0].realOrderID.payMode,"disMode":o[0].realOrderID.disMode,"realname":o[0].realOrderID.userID.realName,"addr":o[0].realOrderID.userID.address,"state":o[0].realOrderID.state,"time1":o[0].realOrderID.delTime,"time2":o[0].realOrderID.recTime,"time3":o[0].realOrderID.accTime}
    infolist=[]
    print("infolist")
    for foo in o:
        subinfo={"id":foo.medicineID_id,"medName": foo.medicineID.generalName, "class": foo.medicineID.classfication,"number":foo.number,"price":foo.medicineID.price,"total":round(int(foo.number)*float(foo.medicineID.price),3)}
        infolist.append(subinfo)
    info["infolist"]=infolist
    return info

def paying(id,paymode,delmode):
    RealOrder.objects.filter(id = id).update(state="未发货")
    RealOrder.objects.filter(id=id).update(payMode= paymode)
    RealOrder.objects.filter(id=id).update(disMode=delmode)

def arrive(id):
    RealOrder.objects.filter(id= id ).update(state = "已送达")