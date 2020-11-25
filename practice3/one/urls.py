from django.urls import path
from one import views

app_name='one'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='user_login'),
    path('register/',views.user_register,name='user_register'),
    path('info/',views.user_info,name='user_info'),
    path('logout/',views.user_logout,name='user_logout'),
]
