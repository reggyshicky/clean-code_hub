from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('', views.homepage, name="homepage"),
    path('login/', views.login, name="login"),
    path('admin/', views.admin_homepage, name="admin_homepage"),
]