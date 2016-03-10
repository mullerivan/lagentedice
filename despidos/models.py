from __future__ import unicode_literals
from accounts.models import User
from django.db import models

# Create your models here.
class Dismissal(models.Model):
    dismissal_date = models.CharField('Fecha del despido:',max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    workplace = models.CharField('Lugar donde trabajaba:',max_length=70)
    comment = models.CharField('Comentario:', max_length=140)

