from django.db import models

# Create your models here.

# Contact model 

class Contact(models.Model):
    slno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from - ' +self.name

# 