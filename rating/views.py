from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Project, Profile, ratings
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
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
