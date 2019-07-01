from userModel.models import Medicine,ImageMedicine,User,Order,Cart,RealOrder
from django.shortcuts import render
import datetime
from datetime import datetime
from django.db.models import Max
from django.db import connection
from userModel.models import RealOrder,Order
from django.utils import timezone

def dictfetchall(cursor):
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]


def getOrder(userName):
    u_id_r = User.objects.raw('select * from usermodel_user where userName = "' + userName + '"')
    u_id = u_id_r[0].id
    print(u_id)
    o = RealOrder.objects.raw('select * from usermodel_realorder where userID_id = ' + str(u_id))
    goods = []
    for foo in o:
        goods.append(str(foo.id))
    result = Order.objects.raw('select * from usermodel_order where realOrderID_id in (' + ",".join(goods) + ')')
    medicine = []
    length = 0
    for foo in result:
        medicine.append(str(foo.medicineID_id))
        length += 1

    print("length", length)
    order_info = []
    print("order_info")
    for i in range(0, length):
        print("ssss")
        result_img = ImageMedicine.objects.raw(
            'select * from usermodel_imagemedicine where medicineID_id =' + str(result[i].medicineID_id))
        print(result[i].medicineID_id)
        number = int(result[i].number)
        info = {'id': result[i].id, 'img': result_img[0].imageUrl,
                'medicine_name': result_img[0].medicineID.generalName,
                'produceCode': result_img[0].medicineID.approvalNumber, 'quatity': result[i].number,
                'state': result[i].realOrderID.state, 'date': result[i].realOrderID.placeTime,
                'price': round(number * float(result_img[0].medicineID.price),3)}
        order_info.append(info)
    print("order_info")
    return order_info

def setOrder(u):
    with connection.cursor() as cursor:
        try:
            print("mmmmmmmmmmmmmmmmmmmmmmmm")
            sql = "SELECT id FROM usermodel_user User WHERE " \
                      "User.userName = %s"
            cursor.execute(sql, [u])
            u_id=cursor.fetchone()[0]
            print(u_id)

            sql = "SELECT number,medicineID_id FROM usermodel_cart Cart WHERE " \
                  "Cart.userID_id = %s"
            cursor.execute(sql, [u_id])
            cart_result = dictfetchall(cursor)
            print(cart_result)
            print("eeeeeeeeeeeeeee")
            realOrder = RealOrder(placeTime=timezone.now(), state='未结账',
                        payMode='微信'
                        , disMode='顺丰快递', userID_id=u_id,
                        delTime=timezone.now(), recTime=timezone.now(),
                                  accTime=timezone.now())
            realOrder.save()
            print("qqqqqqqqqqqqqqqqqqqq")
            sql = "SELECT id FROM usermodel_realorder Rorder ORDER BY id desc limit 1"
            cursor.execute(sql)
            print("oooooooooooooooooo")
            realOrder_id=int(cursor.fetchone()[0])
            print(realOrder_id)
            print(cart_result[0]['medicineID_id'])
            for i in range(0,len(cart_result)):
                order = Order(medicineID_id=int(cart_result[i]['medicineID_id']),
                          number=cart_result[i]['number'],
                          realOrderID_id=realOrder_id)
                order.save()
            return realOrder_id
        except Exception as e:

            print(e)
            return -1

