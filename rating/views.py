from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Project, Profile, ratings
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm
# Create your views here.
def index(request):
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