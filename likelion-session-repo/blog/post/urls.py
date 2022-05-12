from . import views
from django.urls import path

urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('writing/', views.writing, name="writing"),
    path('', views.main, name="main"),

]
