# coding:utf8
from django.http import HttpResponse
import urllib2
import cookielib
from django.views.decorators.csrf import csrf_exempt
from app.models import User

# 使用POST方法获取参数时，需要在发送的头部增加 Content-Type：application/x-www-form-urlencoded的配置，否则只能在request.BODY中取值
@csrf_exempt
def register(request):
    if request.method == 'GET':
        return HttpResponse('注册页面')
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username is None or password is None:
            return HttpResponse({'success': False, 'message': '数据不能为空'})
        user = User()
        user.username = username
        user.password = password
        user.save()
        return HttpResponse({'success': True, 'message': '注册成功'})

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return HttpResponse('登陆页面')
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_message = '登陆失败'
        try:
            user = User.objects.get(username=username, password=password)
            res_message = '登陆成功'
        except Exception as e:
            print str(e)
        res_msg = {
            'success': True,
            'message': res_message
        }
        return HttpResponse(res_msg)