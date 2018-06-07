from django.shortcuts import render
from .models import *
# Create your views here.


def students(request):

    stu_list = Student.objects.all()

    return render(request,'students.html',{'stu_list':stu_list})



