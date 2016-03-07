from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Dismissal(models.Model):
    dismissal_date = models.CharField('Fecha del despido:')
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    workplace = models.CharField('Lugar donde trabajaba:',max_lenght=70)
    comment = models.Charfield('Comentario:', max_lenght=140)



