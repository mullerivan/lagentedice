# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:
from django.views.generic.base import TemplateView


__all__ = (
    'HometView',    
)


class HometView(TemplateView):    
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
    	#aca se hacen las cosas
        return super(HometView, self).get(request, *args, **kwargs)    
