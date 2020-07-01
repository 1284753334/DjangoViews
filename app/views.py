import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def hello(request):
    response = HttpResponse()
    response.content = "德玛西亚"
    #修改状态 页面正常访问
    # response.status_code = 404
    # response.write("正在排队，请稍候")
    # response.flush()
    return response


def get_ticket(request):
    # if  random.randrange(10)>5:
    #     return HttpResponseRedirect('/app/hello')
    #
    # return HttpResponse("恭喜你抢到十一回家的票")
    url = reverse("app:hello")
    print(url)
    #return HttpResponseRedirect(url)、
    return redirect(url)


def get_info(request):
    data ={
        'status':200,
        'msg':"ok",
    }
    return JsonResponse(data= data)


def set_cookie(request):
    response = HttpResponse('设置cookie')
    response.set_cookie("username","Rose")
    return response


def get_cookie(request):
    username = request.COOKIES.get('username')

    return HttpResponse(username)


def login(request):
    return render(request,'login.html')


def do_login(request):
    uname = request.POST.get('uname')
    # response =HttpResponse('登陆成功')
    response = HttpResponseRedirect(reverse('app:mine'))
    # 设置cookie
    #response.set_cookie('uname',uname,max_age=60)
    # 设置加盐cookie
    response.set_signed_cookie('content',uname,'Rock')
    return response


def mine(request):
    #uname = request.COOKIES.get('content')
    #解密cookie
    #  uname = request.get_signed_cookie('content',salt='Rock')
    try:
        uname = request.get_signed_cookie('content',salt='Rock')
        if uname:
            # return HttpResponse(uname)

            return render(request, 'mine.html', context={'uname': uname})
    except Exception as e:
        print('获取失败')

    return redirect('app:login')


    # return HttpResponse(uname)


def logout(request):
    response = redirect(reverse('app:login'))
    response.delete_cookie('content')

    return response