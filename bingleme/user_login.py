from django.http import HttpResponse
from userModel.models import User
from django.shortcuts import render
from django.db import connection
def user_login(request):
    with connection.cursor() as cursor:
        try:
            if (request.POST['password']=='' or request.POST['user']==''):
                raise Exception("有空值！")
            pwd=request.POST['password']
            user=request.POST['user']
            sql = "SELECT * FROM usermodel_user User WHERE " \
                      "(User.username=%s or User.email=%s) and" \
                      " User.password=%s"
            cursor.execute(sql, [user,user,pwd])
            if(cursor.fetchone()==None):
                raise Exception("用户不存在或密码不匹配！")
            response = render(request, 'index.html', {"myuser":user,"myalert": '登陆成功！'})
            response.set_cookie('user', request.POST['user'], max_age=604800)
            return response
        except Exception as e:
            print(e)
            return render(request, 'login.html', {"myalert": e})


