from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CompanyListView.as_view(), name='list'),
    url(r'^new-client/$', views.CompanyCreateView.as_view(), name='create')
]