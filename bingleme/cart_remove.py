from django.http import HttpResponse
from userModel.models import Medicine
from userModel.models import User
from django.db import connection
from .cart_show import cart_show

def cart_remove(request):
    with connection.cursor() as cursor:
        user_name = request.COOKIES.get('user')
        sql = "SELECT * FROM usermodel_user User WHERE " \
              "User.userName = %s "
        cursor.execute(sql, [user_name])
        result = cursor.fetchone()
        user_id = result[0]
        keyword = request.GET.get("id")
        print(keyword)
        sql = "Delete From usermodel_cart WHERE " \
              "medicineID_id = %s and  userID_id = %s"
        cursor.execute(sql, [keyword,user_id])
        return cart_show(request)