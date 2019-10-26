from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to = 'pictures/')
    bio= models.CharField(max_length=30)
    user= models.ForeignKey(User)
    def save_profile(self):
        self.save()
    @classmethod
    def search_by_name(cls,search_term):
        project = cls.objects.filter(name__icontains=search_term)
        return project
class Project(models.Model):
    image_path = models.ImageField(upload_to = 'pictures/')
    project_title= models.CharField(max_length=30)  
    description = models.CharField(max_length=200)
    link =models.CharField(max_length=1200)
