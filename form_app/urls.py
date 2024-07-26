from django.urls import path
from . import views


app_name = "forms"
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.Login_page.as_view(),name = "login"),
    path('thank_you/',views.Thank_youView.as_view(),name= 'thank_you'),
    path('login_list/',views.Login_listsView.as_view(),name='login_list'),
    path('single_view/<int:pk>',views.Login_single_View.as_view(),name='single_view'),
    path('cookies/',views.cookies_demo,name='cookies_demo'),
]
