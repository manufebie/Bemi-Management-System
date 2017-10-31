from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Django's Authentication Views
    url(r'^$', auth_views.login, name='login',
        kwargs={'redirect_authenticated_user': True}), # kwargs argument redirect user if user is already logged in
    url(r'logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'),

    # Dashboard home
    url(r'^dashboard/$', views.DashboardHomeView.as_view(), name='dashboard'),
    
    # Includes
    url(r'^e/', include('employees.urls', namespace='employees')),  
    url(r'^tasks/', include('tasks.urls', namespace='tasks')),
    url(r'^doc/', include('documents.urls', namespace='documents')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns