from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import BaseCreateView
from django.urls import reverse_lazy


from .models import Task
from .forms import TaskCreateForm


class TaskListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView, BaseCreateView):
    queryset = Task.objects.order_by('-timestamp')
    form_class = TaskCreateForm
    success_message = 'Task successfully created! %(name)s was added.'

    template_name = 'tasks/task_list.html'
    
    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(TaskListCreateView, self).get_context_data(**kwargs)
        return context

    # Associates tasks to authenticated user when creating a new task
    def form_valid(self, form):
        task = form.save(commit=False)
        task.employee = self.request.user
        # task.save()
        return super(TaskListCreateView, self).form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')