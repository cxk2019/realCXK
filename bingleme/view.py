from django.shortcuts import render
from os import remove
from django.db import connection
from .user_index_func import checkClassification,getHeatMedicine
from .user_order import getOrder,setOrder
from .user_orderInfo import orderInfo,checkOrder,arrive,paying
from userModel.models import Cart,Order,User,Medicine,ImageMedicine
from .edit_medicine import edit_medicine
def nextOrder(request):
    with connection.cursor() as cursor:
        try:
            user_name = request.COOKIES.get('user')
            sql = "SELECT * FROM usermodel_user User WHERE " \
                  "User.userName = %s "
            cursor.execute(sql, [user_name])
            result = cursor.fetchone()
            user_id = result[0]
            num = request.GET.get('num')
            keyword = request.GET.get('product_id')

            sql = "SELECT * FROM usermodel_cart Cart WHERE " \
                  "Cart.medicineID_id = %s "
            cursor.execute(sql, [keyword])
            if (cursor.fetchone() != None):
                sql = "Update usermodel_cart Cart " \
                      "Set Cart.number = Cart.number+%s WHERE " \
                      "Cart.medicineID_id = %s "
                cursor.execute(sql, [num, keyword])
            else:
                cart = Cart(number=num, medicineID_id=keyword,
                            userID_id=user_id)
                cart.save()
            return cart_show(request)
        except Exception as e:

            return render(request, 'index.html', {"myalert": e})
def dictfetchall(cursor):
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
def cart(request):
    return render(request,'cart.html',{"myuser": request.COOKIES.get('user')})

def category(request):
    return render(request,'category.html',{"myalert":0,"myuser": request.COOKIES.get('user')})


def grounding(request):
    return render(request,'grounding.html',{"myuser": request.COOKIES.get('user')})

def index(request):
    u=0
    if 'user' in request.COOKIES:
        u=request.COOKIES['user']

    classes = checkClassification()
    h_medicine = getHeatMedicine()
    return render(request,'index.html',{"myuser":u,"classfication":classes,"h_medicine1":h_medicine[0],"h_medicine2":h_medicine[1]})

def order_history(request):
    u = 0
    if 'user' in request.COOKIES:
        u = request.COOKIES['user']
        orderList = getOrder(u)
        return render(request, 'order-history.html', {"list": orderList,"myuser": request.COOKIES.get('user')})
    else:
        return index(request)

def loginOut(request):
    classes = checkClassification()
    h_medicine = getHeatMedicine()
    response = render(request, 'index.html',{"myuser": 0,"myalert": 0, "classfication": classes, "h_medicine1": h_medicine[0], "h_medicine2": h_medicine[1]})
    response.delete_cookie('user')
    response.delete_cookie('isAdmin')
    return response

def order_information(request):
    id = request.GET.get('id')  # order主键
    if (id):
        info = orderInfo(id)
        info = checkOrder(info)  # 放进去的市realid
        info["myuser"] = request.COOKIES.get('user')

        return render(request, 'order-information.html',info)
    else:
        return index(request)

def hasArrive(request):
    id = request.GET.get('id')
    if (id):
        info = orderInfo(id)
        arrive(info)
        info = checkOrder(info)
        return render(request, 'order-information.html', info)
    else:
        return index(request)

def pay(request):
    id=request.GET.get('id')
    paymode=request.POST.get("paymode")
    delmode=request.POST.get("delMode")

    if(id):
        if(paymode and delmode ):
            paying(id,paymode,delmode)
            #清空购物车

            return order_history(request)
        else:
            return order_information(request)
    else:
        return index(request)

def newOrder(request):
    u = 0
    if 'user' in request.COOKIES:
        u = request.COOKIES['user']
        i = setOrder(u)
        u_id_r = User.objects.raw('select * from usermodel_user where userName = "' + u + '"')
        u_id = u_id_r[0].id

        Cart.objects.filter(userID_id=u_id).delete()
        i = str(i)
        info = checkOrder(i)  # 放进去的市realid
        info['myuser'] = request.COOKIES.get('user')
        print("sdfsfsdddddddddddddddd")
        print(info)
        sum_price=0
        for item in info['infolist']:
            sum_price+=int(item['number'])*float(item['price'])
        info['sum_price']=sum_price
        return render(request, 'order-information.html', info)
    else:
        return index(request)


def medicine_list(request):
    result = Medicine.objects.all()
    list = []
    for medicine in result:
        imagelist = ImageMedicine.objects.filter(medicineID_id=medicine.id)
        imageUrl = imagelist[0].imageUrl
        info = {"id": medicine.id, "image": imageUrl, 'generalName': medicine.generalName, 'approvalNumber': medicine.approvalNumber,
                'goodsName': medicine.goodsName, "enterpriseName": medicine.enterpriseName, 'price': medicine.price}
        list.append(info)
    response = render(request, 'medicine-list.html', {"list": list})
    return response

def delete_image(request):
    imageUrl = request.GET.get('imgUrl','')
    img = ImageMedicine.objects.get(imageUrl=imageUrl)
    remove('./static/image/medicine/%s' % imageUrl)
    img.delete()
    #删除结束，重新刷新页面
    return edit_medicine(request)

def quickview(request):
    m_id=request.GET.get('item')
    with connection.cursor() as cursor:
        try:
            sql = "SELECT * FROM usermodel_medicine Medicine WHERE " \
                  "Medicine.id=%s"
            cursor.execute(sql, [m_id])
            item = dictfetchall(cursor)[0]

            sql = "SELECT * FROM usermodel_imagemedicine img WHERE " \
                  "img.medicineID_id=%s"

            cursor.execute(sql, [item['id']])
            result=dictfetchall(cursor)
            return render(request, 'quickview.html', {'item': item,'result':result})
        except Exception as e:


            return render(request, 'quickview.html', {"myalert": e})

def register(request):
    return render(request,'register.html',{"myalert":0})

def login(request):
    return render(request,'login.html')

def product(request):
    medicine_id = request.GET.get('medicine_id')

    with connection.cursor() as cursor:
        try:
            sql = "SELECT * FROM usermodel_imagemedicine img WHERE " \
                  "img.medicineID_id=%s"
            cursor.execute(sql, [medicine_id])
            #result_img里存放着所有的当前药品的图片记录
            result_img=dictfetchall(cursor)


            sql = "SELECT * FROM usermodel_medicine Medicine WHERE " \
                  "Medicine.id=%s"
            cursor.execute(sql, [medicine_id])
            # result_medicine里存放着所有的当前药品的记录
            result_medicine=dictfetchall(cursor)

            return render(request, 'product.html', {"myuser": request.COOKIES.get('user'),'result_img': result_img,'result_medicine':result_medicine[0]})
        except Exception as e:

            return render(request, 'product.html', {"myalert": e})



