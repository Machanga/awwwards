from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,VoteForm,ProfileForm
from .models import Project,Vote,Profile
from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        if not Profile.objects.filter(user = request.user).exists():
            return redirect('edit_profile', username=request.user.username)
    projects = Project.objects.all()
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"project": searched_project})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html',{"message":message})

def profile(request,username):
    current_user = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    projects = Project.objects.filter(profile=profile)
    return render(request,'profile.html',{"profile":profile,"projects":projects})

@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect(reverse('index'))
    else:
        form = NewProjectForm()
    return render(request,'project.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.filter(user = request.user).first()
    projects = Project.objects.filter(user=profile.user).all()

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('profile'))
    else:
        form = EditProfile()
    return render(request,'profile.html',{'form':form})