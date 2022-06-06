from django.urls import include, path
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.ImageList.as_view(), name='list'),
    path('new/image', views.new_image, name='new-image'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/profile/', views.user_profile, name='user-profile'),
   
    
    
    
]
