from userModel.models import Medicine,ImageMedicine,User,Order,RealOrder
from django.shortcuts import render
import datetime

def getAdminOrder(request):
    result = RealOrder.objects.raw('select * from usermodel_realorder where state = "未发货"')
    print(result)
    length=0
    for foo in result:
        length+=1
    order_info = []
    for i in range(0,length):
        orderlist = Order.objects.filter(realOrderID=result[i].id)
        total = 0
        for order in orderlist:
            total += float(order.medicineID.price) * order.number
            time = datetime.datetime.strftime(result[i].placeTime,'%Y-%m-%d %H:%M')
        info={'id':result[i].id,'paymode':result[i].payMode,'dismode':result[i].disMode,'userId': result[i].userID.userName,'address': result[i].userID.address,'place_time':time,'price':'%.2f'%total}
        order_info.append(info)
    return render(request,'admin-orderlist.html',{'list':order_info})

