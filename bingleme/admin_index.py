from django.shortcuts import render
from django.http import HttpResponse


def adminIndex(request):
    return render(request,'admin-index.html')
