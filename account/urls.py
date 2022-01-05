from django.urls import path
from . import views
from django.contrib.auth import views as auth
from django.urls import include


urlpatterns = [
    #path('login/',views.user_login,name='login')
    
    
    path('', include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
    path('users/',views.user_list,name='user_list'),
    path('users/follow',views.user_follow,name='user_follow'),
    path('users/<username>',views.user_detail,name='user_detail'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
