from django.http import HttpResponse
from userModel.models import Medicine
from userModel.models import User
from userModel.models import Cart
from django.db import connection
from django.shortcuts import render
from .cart_show import cart_show

def cart_add(request):
    with connection.cursor() as cursor:
        try:
            user_name = request.COOKIES.get('user')
            sql = "SELECT * FROM usermodel_user User WHERE " \
                  "User.userName = %s "
            cursor.execute(sql, [user_name])
            result = cursor.fetchone()
            user_id = result[0]
            num = request.POST['quantity']
            if num == '0':
                raise Exception("数量不得为0")
            keyword = request.POST['product_id']
            sql = "SELECT * FROM usermodel_cart Cart WHERE " \
                  "Cart.medicineID_id = %s "
            cursor.execute(sql, [keyword])
            if (cursor.fetchone() != None):
                sql = "Update usermodel_cart Cart " \
                      "Set Cart.number = Cart.number+%s WHERE " \
                      "Cart.medicineID_id = %s "
                cursor.execute(sql, [num, keyword])
            else:
                cart = Cart(number = request.POST['quantity'], medicineID_id = request.POST['product_id'],
                            userID_id = user_id )
                cart.save()
            return cart_show(request)
        except Exception as e:
            print(e)
            return render(request, 'index.html', {"myalert": e})