from django.http import HttpResponse
from userModel.models import Medicine
from django.shortcuts import render,redirect
from django.db import connection
def dictfetchall(cursor):
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
def search_medicine(request):
    with connection.cursor() as cursor:
        try:
            keyword=request.POST['search']
            if keyword=='':
                raise Exception("输入为空！")
            print("qqqqqqq")
            query_param = '%'+keyword+'%'
            sql = "SELECT * FROM usermodel_medicine Medicine WHERE " \
                      "Medicine.generalName LIKE %s or" \
                      " Medicine.function LIKE %s"
            print("xxxxxxxxx")
            cursor.execute(sql, [query_param,query_param])
            print("wwwwwww")
            if(cursor.fetchone()==None):
                raise Exception("未找到！")
            result=dictfetchall(cursor)
            print("sdfdsfsdfdsfdsf")
            print(result)
            print("bbbbbbbb")
            response = render(request, 'category.html', {"myuser": request.COOKIES.get('user'),"medicine_list":result})
            return response
        except Exception as e:
            print(e)
            return render(request, 'index.html', {"myalert": e})


