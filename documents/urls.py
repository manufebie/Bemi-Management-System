from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListCreateView.as_view(), name='list'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DocumentDeleteView.as_view(), name='delete'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.DocumentUpdateView.as_view(), name='update'),
    #url(r'^upload/$', views.DocumentCreateView.as_view(), name='upload'),
]