from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from Portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^projects/(?P<project_id>\D+)/', views.project, name="project"),
)

