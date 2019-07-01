from django.http import HttpResponse
from userModel.models import Medicine
from userModel.models import User
from userModel.models import Cart
from django.db import connection
from django.shortcuts import render
from .cart_show import cart_show

def cart_update(request):
    with connection.cursor() as cursor:
        try:
            num = request.POST['quantity']
            keyword = request.POST['m_id']
            if num == '0':
                raise Exception("数量不得为0")
            sql = "Update usermodel_cart Cart " \
                  "Set Cart.number = %s WHERE " \
                  "Cart.medicineID_id = %s "
            cursor.execute(sql,[num,keyword])
            return cart_show(request)
        except Exception as e:
            print(e)
            return render(request, 'index.html', {"myalert": e})



