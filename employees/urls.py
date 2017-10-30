from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EmployeeListView.as_view(), name='list'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^(?P<lastname>[\w-]+)/$', views.EmployeeProfileDetailView.as_view(), name='detail'),
]