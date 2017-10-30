from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView

from .models import Employee
from .forms import SignUpForm


class RegistrationView(SuccessMessageMixin, CreateView):
   model = Employee
   form_class = SignUpForm
   success_message = 'Succesfully registered, login in with your email'
   template_name = 'registration/register.html'
   
   def form_valid(self, form):
       return super(RegistrationView, self).form_valid(form)


class EmployeeProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employees/employee_detail.html'

    def get_object(self):
        lastname = self.kwargs.get('lastname')
        if lastname is None:
            raise Http404
        return get_object_or_404(Employee, lastname__iexact=lastname, is_active=True)


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'