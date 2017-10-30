from django.views.generic import ListView, CreateView
#from django.views.generic.edit import BaseCreateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CompanyCreateForm

from .models import Company


class CompanyListView(LoginRequiredMixin,ListView):
    model = Company

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'clients:client_form.html'


#class CompanyListAndCreateView(LoginRequiredMixin, ListView, BaseCreateView):
#    model = Company
