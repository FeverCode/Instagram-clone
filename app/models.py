import email
from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
        


class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    captions = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default='0',null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    @classmethod
    def search_by_profile(cls, search_term):
        name = search_term = cls.objects.filter(profile__username__icontains=search_term)
        return name
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()

