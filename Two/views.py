import hashlib
import random
import time

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from Two.models import Student


def hello(request):
    return HttpResponse('hello  Two')


def login(request):
    if request.method == 'GET':
        return render(request,'two_login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        request.session['username'] = username

        return HttpResponse( '登录成功')


def mine(request):
    username = request.session.get('username')
    return render(request,'two_mine.html',context=locals())

def logout(request):
    # response = request.session.get('uname')
    response = redirect(reverse('two:mine'))
    # 删除 cookie  缺点 session 还在
    #response.delete_cookie('sessionid')
    #  删除 session
    #del request.session['username']、
    # 删除cookie 和 session
    request.session.flush()

    return response


def register(request):
    if request.method =='GET':
        return render(request,'student_register.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student()
            student.s_name =username
            student.s_password = password
            student.save()
        except Exception as e:
            return redirect(reverse('two:register'))

        return  HttpResponse('注册成功')


def stslogin(request):
    if request.method == 'GET':
        return render(request, 'student_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        students =Student.objects.filter(s_name=username).filter(s_password=password)
        if students.exists():
            student = students.first()
            # ip = request.META.get('REMOTE_ADDR')
            # token = generate_token(ip,username)
            # student.s_token = token
            # student.save()

            response = HttpResponse('用户登陆成功')
            # response.set_cookie('token',token)

            return HttpResponse
        return redirect(reverse('two:stslogin'))

def generate_token(ip,username):
    c_time = time.ctime()
    r = username

    return hashlib.new('md5', (ip + c_time + r).encode('utf-8')).hexdigest()
