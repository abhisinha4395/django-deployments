from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns=[
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login")
]
