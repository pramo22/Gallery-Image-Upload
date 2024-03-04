from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,null=True,blank=True )
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Imageadd(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.FileField(upload_to='static/videos/%Y', null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title