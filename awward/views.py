
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewpostForm
from  .models import Profile,Project

# Create your views here.
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()
    return render(request,'welcome.html',{ "projects":projects})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewpostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            
            project.save()
        return redirect('welcome')

    else:
        form = NewpostForm()
    return render(request, 'new_post.html', {"form": form})
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_project_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-file/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-file/search.html',{"message":message})