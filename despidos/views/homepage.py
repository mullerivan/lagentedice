# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from despidos.forms import DismissalForm




__all__ = (
        'HomeView', 'NewDismissalView',
)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['comments'] = range(1,5)
        return context

    def get(self, request, *args, **kwargs):
        #aca se hacen las cosas
        return super(HomeView, self).get(request, *args, **kwargs)

class NewDismissalView(CreateView):
    template_name = 'new_dismissal.html'
    form_class = DismissalForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewDismissalView, self).form_valid(form)
