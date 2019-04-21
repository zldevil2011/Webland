from django.conf.urls import include, url
from app.views.index import index
from app.views.devices.index import device_list, device_data, all_device_data, total_data_sum, total_abnormal_sum, total_device_sum
import user_urls

urlpatterns = [
    url('index/$',index, name="index"),
    url('device_list/$', device_list, name="device_list"),
    url('device_data/(\d+)/$', device_data, name="device_data"),
    url('all_device_data/$', all_device_data, name="all_device_data"),
    url('user/', include(user_urls)),


    url('total_data_sum/$', total_data_sum, name="total_data_sum"),
    url('total_abnormal_sum/$', total_abnormal_sum, name="total_abnormal_sum"),
    url('total_device_sum/$', total_device_sum, name="total_device_sum")
]
