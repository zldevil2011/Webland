from django.conf.urls import include, url
from app.views import index

urlpatterns = [
    url(r'index/$',index, name="index")
]
