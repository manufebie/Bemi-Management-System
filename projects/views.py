from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseCreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ProjectForm
from .models import Project


class ProjectListView(LoginRequiredMixin, SuccessMessageMixin, ListView, BaseCreateView):
     queryset = Project.objects.order_by('-id')
     form_class = ProjectForm
     success_message = 'You have successfully started a new project for "%(client)s"'
     #template_name = ''

     def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(ProjectListView, self).get_context_data(**kwargs)
        return context
     

class ProjectDetailView(DetailView):
        model = Project
        context_object_name = 'project'