from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url('^$',views.index,name = 'index'),
    url(r'^post_project$',views.new_project,name='new_project'),
    url(r'^search/$',views.search_results,name='search_results'),
    url(r'^profile/(?P<username>\w{0,60})',views.profile,name='profile'),
    url(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name='edit_profile'),
    url(r'^project/(\d+)',views.project,name='project'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)