from django.urls import path
from app import views

urlpatterns = [
    path('new/image', views.new_image, name='new-image')
    
]
