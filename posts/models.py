from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

"""
Clase  model of the posts
"""
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile',on_delete= models.CASCADE)
    title = models.CharField(max_length=255)
    photo = CloudinaryField('photo')
    likes = models.IntegerField(default=0,blank=True,null=True)
    #photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.created,self.user.username)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile',on_delete= models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return '{} liked {}'.format(self.user.username,self.post.title)