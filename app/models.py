from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()
    
    
    def __str__(self):
        return self.profile_photo
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()




class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    captions = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.image
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()

