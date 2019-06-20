from django.http import HttpResponse
from userModel.models import User
from django.shortcuts import render
def user_register(request):
    try:
        if (request.POST['password']=='' or request.POST['confirm']==''
                or request.POST['user']=='' or request.POST['telephone']==''
                or request.POST['firstname']=='' or request.POST['address_1']==''
                or request.POST['email']=='' or request.POST['postcode']==''):
            raise Exception("有空值！")
        if request.POST['password']!=request.POST['confirm']:
            raise Exception("密码不一致！")
        user=User(userName=request.POST['user'],password=request.POST['password'],phone=request.POST['telephone']
              ,realName=request.POST['firstname'],address=request.POST['address_1'],
              email=request.POST['email'],postalCode=request.POST['postcode'])
        user.save()
        response=render(request,'index.html',{"myuser":request.POST['user'],"myalert":"注册成功！"})
        response.set_cookie('user', request.POST['user'],max_age=604800)
        return response
    except Exception as e:
        print(e)
        x=e
        if e.args[0]==1062:
            x="用户名或手机号已存在！"
        return render(request, 'register.html',{"myalert": x})