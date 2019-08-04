from django.db import models

# Create your models here.
class Project(models.Model):
    '''
    project class for all the projects that will be added to the application
    '''
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=200)

class Profile(models.Model):
    '''
    profile class for all the profiles that will be added to the application
    '''
    profpic = models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length = 500)
    projects = models.ForeignKey(Project)
    contact = models.CharField(max_length=100)