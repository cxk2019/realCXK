from django.http import HttpResponse
from userModel.models import Medicine
from userModel.models import User
from userModel.models import Cart
from django.db import connection
from django.shortcuts import render

def dictfetchall(cursor):
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]

def cart_show(request):
    with connection.cursor() as cursor:
        user_name = request.COOKIES.get('user')
        sql = "SELECT * FROM usermodel_user User WHERE " \
              "User.userName = %s "
        cursor.execute(sql, [user_name])
        result = cursor.fetchone()
        user_id = result[0]
        sql = "SELECT Cart.medicineID_id,Cart.number FROM usermodel_cart Cart WHERE " \
              "Cart.userID_id = %s "
        cursor.execute(sql, [user_id])
        result_item = dictfetchall(cursor)
        n = len(result_item)
        result_cart = []
        total_price=0
        for i in range(0,n):
            sql = "SELECT * FROM usermodel_medicine Medicine WHERE " \
                  "Medicine.id = %s "
            cursor.execute(sql, [result_item[i]['medicineID_id']])
            temp=dictfetchall(cursor)[0]
            temp['price']=float(temp['price'])
            result_item[i]['item']=temp
            result_item[i]['singleTotalPrice']=round(temp['price']*result_item[i]['number'],3)
            total_price+=result_item[i]['singleTotalPrice']
        total_price=round(total_price,3)
        response = render(request, 'cart.html', {"myuser": request.COOKIES.get('user'),"cart_list": result_item,"total_price":total_price,"myuser": request.COOKIES.get('user')})
        return response

# def item_update(request):
#
#
# def item_remove(request):

