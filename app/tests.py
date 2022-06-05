from django.test import TestCase
from .models import Profile, Image

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile = Profile(profile_photo='https://res.cloudinary.com/dzqbzqjqw/image/upload/v1559098981/profile_photo_qjqjqj.jpg', bio='I am a software developer')
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    # Testing Save Method
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles), 1)
    
    # Testing Delete Method
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles), 0)


    
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile = Profile(profile_photo='https://res.cloudinary.com/dzqbzqjqw/image/upload/v1559098981/profile_photo_qjqjqj.jpg', bio='I am a software developer')
        self.profile.save_profile()
        
        self.image = self.profile.image_set.create(image='https://res.cloudinary.com/dzqbzqjqw/image/upload/v1559098981/image_qjqjqj.jpg', name='image', captions='This is a caption', likes=0, comments='This is a comment')
        
    # Testing instance
    def test_instance(self):
         self.assertTrue(isinstance(self.image, Image))
         
    # Testing Save Method
    def test_save_method(self):       
        self.image.save_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)
        
    # Testing Delete Method
    def test_delete_method(self):       
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 0)
    

    