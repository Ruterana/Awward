from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('This is Awward app')
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')