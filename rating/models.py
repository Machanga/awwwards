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