from django.conf.urls import include, url
from app.views.index import index

urlpatterns = [
    url('index/$',index, name="index")
]
