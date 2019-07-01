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
def classify_medicine(request):
    with connection.cursor() as cursor:
        try:
            class_name=request.GET.get('class_name')
            sql = "SELECT * FROM usermodel_medicine Medicine WHERE " \
                      "Medicine.classfication=%s"
            cursor.execute(sql, [class_name])
            result=dictfetchall(cursor)
            print(result)
            response = render(request, 'category.html', {"myuser": request.COOKIES.get('user'),"medicine_list":result})
            return response
        except Exception as e:
            print(e)
            return render(request, 'index.html', {"myalert": e})


