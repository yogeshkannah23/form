from django.urls import path
from . import views


app_name = "forms"
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.Login_page.as_view(),name = "login"),
    path('thank_you/',views.Thank_youView.as_view(),name= 'thank_you'),
]
