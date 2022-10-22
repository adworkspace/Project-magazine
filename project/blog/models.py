from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
 

# Create your models here.

# Creating Post model HERE

class Post(models.Model):
    slno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.CharField(max_length=25)
    language=models.CharField(max_length=15)
    author=models.CharField(max_length=40)
    postImage=models.ImageField(upload_to='static/image/post_img')
    slug=models.CharField(max_length=100)
    timeStamp=models.DateTimeField(blank=True)
   

    def __str__(self):
        return self.title + ' by ' + self.author


class Paint(models.Model):
    painter=models.CharField(max_length=25)
    paint_title=models.CharField(max_length=30)
    painting=models.ImageField(upload_to='static/image/painting')
    slug=models.CharField(max_length=30)
    timeStamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paint_title+' by '+self.painter
    
class BlogComment(models.Model):
    slno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[:12]+"... by "+self.user.username
    