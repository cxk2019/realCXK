from django.http import HttpResponse
from userModel.models import User
from django.shortcuts import render,redirect
from django.db import connection
from .user_index_func import checkClassification,getHeatMedicine
def user_login(request):
    with connection.cursor() as cursor:
        try:
            if (request.POST['password']=='' or request.POST['user']==''):
                raise Exception("有空值！")
            pwd=request.POST['password']
            user=request.POST['user']
            sql = "SELECT isAdmin FROM usermodel_user User WHERE " \
                      "(User.username=%s or User.email=%s) and" \
                      " User.password=%s"
            cursor.execute(sql, [user,user,pwd])
            result1=cursor.fetchone()
            if(result1==None):
                raise Exception("用户不存在或密码不匹配！")
            print("nnnnnnnnnnnnnnn")
            print(result1[0])
            response=0
            if result1[0]=='0':
                classes = checkClassification()
                h_medicine = getHeatMedicine()
                response = render(request, 'index.html', {"myuser": user, "myalert": '登陆成功！',"classfication": classes, "h_medicine1": h_medicine[0],
                               "h_medicine2": h_medicine[1]})
            else:
                response = render(request, 'admin-index.html',{"myuser": user})
            response.set_cookie('user', request.POST['user'], max_age=604800)
            response.set_cookie('isAdmin', result1[0], max_age=604800)
            return response
        except Exception as e:
            print(e)
            return render(request, 'login.html', {"myalert": e})


