from django.shortcuts import render
from Portfolio.models import Project
from django.http import HttpResponse

# Create your views here.

def index(request):
    projects = Project.objects.get_queryset()
    context = {}
    context['projects'] = projects
    return render(request, 'Portfolio/index.html', context)

def project(request, project_id):
    project = Project.objects.get_queryset().filter(project_id=project_id)[0]
    context = {}
    context['project'] = project
    return render(request, 'Portfolio/project.html', context)

def helloWorld(request):

    return HttpResponse("Hello World")

 def scary(request):
 {
 	return HttRespons("Boo!")
 }