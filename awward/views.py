from django.shortcuts import render
from .models import Profile
# Create your views here.
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    return HttpResponse('This is Awward app')
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-file/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-file/search.html',{"message":message})
# @login_required(login_url='/accounts/login/')