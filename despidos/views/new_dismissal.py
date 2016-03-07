from django.views.generic import CreateView
from despidos.forms import DismissalForm

__all__ = (
        'NewDismissalView',
        )


class NewDismissalView(CreateView):
    template_name = 'new_dismissal.html'
    form_class = DismissalForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewDismissalView, self).form_valid(form)
