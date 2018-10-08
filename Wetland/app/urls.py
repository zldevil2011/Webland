from django.conf.urls import include, url
from app.views.index import index
from app.views.devices.index import device_list, device_data
import user_urls

urlpatterns = [
    url('index/$',index, name="index"),
    url('device_list/$', device_list, name="device_list"),
    url('device_data/(\d+)/$', device_data, name="device_data"),
    url('user/', include(user_urls))
]
