from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TaskListCreateView.as_view(), name='list'),
     url(r'^delete/(?P<pk>[0-9]+)/$', views.TaskDeleteView.as_view(), name='delete'),
    #url(r'^create/$', views.TaskCreateView.as_view(), name='create'),

]
