from django import forms
from .models import Project, Profile

class NewProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        fields = ('title', 'image', 'description', 'url')

class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('profpic', 'bio', 'contact')