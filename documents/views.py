from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DeleteView, UpdateView
from django.views.generic.edit import BaseCreateView 
from django.urls import reverse_lazy

from .forms import DocumentUploadForm
from .models import Document



# Combines both ListView and Create view in one template
class ListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView, BaseCreateView):
    queryset = Document.objects.order_by('-timestamp')
    form_class = DocumentUploadForm
    #success_url = 'documents:list'
    success_message = '%(name)s was successfully added'

    template_name = 'documents/document_list.html'

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(ListCreateView, self).get_context_data(**kwargs)
        return context


class DocumentUpdateView(UpdateView):
    model = Document
    context_object_name = 'doc'
    form_class = DocumentUploadForm
    template_name = 'documents/document_update_form.html'
    

class DocumentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Document
    context_object_name = 'doc'
    #success_message = '%(name)s was successfully deleted'
    success_url = reverse_lazy('documents:list')