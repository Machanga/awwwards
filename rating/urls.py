from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/project$', views.post_project, name='post_project'),
    url(r'myprofile/edit$',views.edit,name='edit'),
    url(r'profile/user/(\d+)/$',views.profile,name='users'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)