from django.conf.urls import include, url
from app.views.users.utils import register, login

urlpatterns = [
    url('register/$',register, name="user_register"),
    url('login/$', login, name="user_login")
]
