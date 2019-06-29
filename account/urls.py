from django.conf.urls import url
from . import views

from django.conf import settings

urlpatterns = [
    url(r'login/$', views.user_login, name='user_login'),
    url(r'logout/$', views.user_logout, name="user_logout"),
    url(r'register/$', views.user_register, name='user_register'),
    url(r'setpassword/$', views.setpassword, name="setpassword"),
    url(r'password_reset/$', views.password_reset, name='password_reset'),
    url(r'password_reset_test/$', views.password_reset_test, name='password_reset_test'),
    url(r'edit_info/$', views.edit_info, name='edit_info'),
    url(r'my_image/$', views.my_image,  name="my_image")
]
