from django.db import models
from BlogApp.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255, blank=False, null = False)
    description = models.CharField(max_length = 255, blank = True, null = True)
    post_date = models.DateTimeField()
    delet_date = models.DateTimeField(null=True)
    category_id =  models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, null=True,on_delete = models.SET_NULL)
    # likes = models.ManyToManyField(User,blank=True, related_name='likes')
     
    def __str__(self):
        return self.title + ' ' + str(self.owner)
