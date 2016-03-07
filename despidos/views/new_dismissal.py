from django.views.generic import CreateView, UpdateView
from despidos.forms import DismissalForm
from django.core.urlresolvers import reverse_lazy
from despidos.models import Dismissal

__all__ = (
        'NewDismissalView',
        'EditDismissalView',
        )


class NewDismissalView(CreateView):
    template_name = 'new_dismissal.html'
    form_class = DismissalForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewDismissalView, self).form_valid(form)

class EditDismissalView(UpdateView):
    form_class = DismissalForm
    success_url = reverse_lazy('home')
    template_name = 'new_dismissal.html'

    def get_object(self, queryset=None):
        obj = Dismissal.objects.get(id=self.kwargs['pk'])
        return obj
