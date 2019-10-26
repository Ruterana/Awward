from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/profile$', views.addprofile, name='profile'),
    url(r'^new/viewprofile$', views.viewprofile, name='viewprofile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)