# coding:utf8
from django.http import HttpResponse
import urllib2
import cookielib


def index(request):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    request = urllib2.Request(url='http://localhost:8080/')
    response = opener.open(request)
    print(response)
    return HttpResponse(response)