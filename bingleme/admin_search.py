from django.http import HttpResponse
from userModel.models import Medicine,ImageMedicine
from django.shortcuts import render,redirect
from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]


def admin_search(request):
    with connection.cursor() as cursor:
        try:
            keyword=request.GET.get('search','')
            if keyword == '':
                raise Exception("输入为空！")
            query_param = '%' + keyword + '%'
            sql = "SELECT * FROM usermodel_medicine Medicine WHERE " \
                  "Medicine.generalName LIKE %s or" \
                  " Medicine.function LIKE %s"
            cursor.execute(sql, [query_param, query_param])
            if (cursor.fetchone() == None):
                raise Exception("未找到！")
            result = dictfetchall(cursor)
            for item in result:
                imagelist = ImageMedicine.objects.filter(medicineID_id=int(item['id']))
                imageUrl = imagelist[0].imageUrl
                print(imageUrl)
                imgdic = {'image': imageUrl}
                item.update(imgdic)
            response = render(request, 'medicine-list.html', {"list":result})
            return response
        except Exception as e:
            print(e)
            return render(request, 'admin-index.html', {"myalert": e})
