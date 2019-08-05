from django.db import models
from django.contrib.auth.models import User

CHOICES=[
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
]
# Create your models here.
class Project(models.Model):
    '''
    project class for all the projects that will be added to the application
    '''
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=200)
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    def save_project(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class Profile(models.Model):
    '''
    profile class for all the profiles that will be added to the application
    '''
    profpic = models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length = 500)
    projects = models.ForeignKey(Project)
    contact = models.CharField(max_length=100)

    def save_profile(self):
        self.save()

class ratings(models.Model):
    design=models.IntegerField(choices=CHOICES)
    usability = models.IntegerField(choices=CHOICES)
    content = models.IntegerField(choices=CHOICES)
    project = models.ForeignKey(Project)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def save_ratings(self):
        self.save()