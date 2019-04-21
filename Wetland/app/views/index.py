# coding:utf8
from django.http import HttpResponse
import urllib2
import cookielib
import json



def index(request):
    # cookie = cookielib.CookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # request = urllib2.Request(url='http://localhost:8080/')
    # response = opener.open(request)
    # print(response)
    res = {
        'name': 'zhaolong',
        'text': '123456',
    }
    response = HttpResponse(json.dumps(res), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
    # return HttpResponse(response)