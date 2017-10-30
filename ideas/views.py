from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import BaseCreateView

from .models import Idea


class IdeaCreateListView(LoginRequiredMixin, ListView, BaseCreateView, SuccessMessageMixin):
    queryset = Idea.objects.order_by('-timestamp')
    fields = ['name', 'content']
    template_name = 'ideas/idea_list.html'
    success_message = 'Your idea has successfully been pinned to the wall'

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(IdeaCreateListView, self).get_context_data(**kwargs)
        return context