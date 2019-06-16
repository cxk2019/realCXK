from django.http import HttpResponse
from userModel.models import User
def user_register(request):
    print("wocao")
    print(request.POST)
    user=User(user_name=request.POST['user'],password=request.POST['password'],phone=request.POST['telephone']
              ,realname=request.POST['firstname'],address=request.POST['address_1'],
              email=request.POST['email'],postal_code=request.POST['postcode'])
    print(user)
    user.save()
    return HttpResponse("<p>注册成功！</p>")