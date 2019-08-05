from django.forms import ModelForm
from .models import Project, Profile, Vote
from django.contrib.auth.models import User

class NewProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        fields = ('title', 'image', 'description', 'url')

class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('profpic', 'bio', 'contact')

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ['project','profile']