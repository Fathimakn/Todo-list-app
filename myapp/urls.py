from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('update/<int:id>/',views.update,name='update'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>',views.delete,name='delete'),

]
