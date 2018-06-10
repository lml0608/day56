from django.shortcuts import render,HttpResponse
from .models import *
import json
# Create your views here.


def students(request):

    cls_list = Classes.objects.all()

    stu_list = Student.objects.all()



    return render(request,'students.html',{'cls_list':cls_list,'stu_list':stu_list})


def add_student(request):
    """
    添加学生
    :param request: 
    :return: 
    """

    response = {'status':True,'message':None}

    try:

        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cls_id')

        obj = Student.objects.create(
            username=u,
            age=a,
            gender=g,
            cs_id=c)

        response['data'] = obj.id

    except Exception as e:

        response['status'] = False
        response['message'] = "用户输入错误！"



    result = json.dumps(response)
    return HttpResponse(result)


