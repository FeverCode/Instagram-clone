from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=30, default='DEFAULT VALUE')
    profile_photo = CloudinaryField('image')
    bio = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.username
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()




class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    captions = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default='0',null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()

