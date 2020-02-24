from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

"""
Model of users profile data extending the User model of auth in django
"""
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(max_length=255,blank=True)
    biography = models.CharField(max_length=500,blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    picture = CloudinaryField('picture',blank=True,null=True)
    # picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    following = models.ForeignKey(Profile,on_delete=models.CASCADE)
    follower = models.ForeignKey(User,on_delete=models.CASCADE)
    followed = models.DateTimeField(auto_now_add=True)