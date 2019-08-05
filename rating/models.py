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
    title = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'images/',blank=True)
    description = models.TextField()
    url = models.URLField(max_length = 40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,null=True)

    def save_project(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class Profile(models.Model):
    profpic = models.ImageField(upload_to = 'images/')
    bio = models.TextField()
    contact = models.CharField(max_length = 40)
    projects = models.ManyToManyField(Project,blank=True,related_name='profile_projects')
    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    def save_profile(self):
        self.save()

class Vote(models.Model):
    design=models.IntegerField(choices=CHOICES)
    usability = models.IntegerField(choices=CHOICES)
    content = models.IntegerField(choices=CHOICES)
    project = models.ForeignKey(Project)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    def save_ratings(self):
        self.save()