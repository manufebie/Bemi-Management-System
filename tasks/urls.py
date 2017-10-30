from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TaskListCreateView.as_view(), name='list'),
    #url(r'^create/$', views.TaskCreateView.as_view(), name='create'),

]
