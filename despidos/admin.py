from django.contrib import admin
from models import Dismissal

class DismissalAdmin(admin.ModelAdmin):
    fields =['dismissal_date', 'workplace', 'comment', 
            'user']

# Register your models here.
admin.site.register(Dismissal, DismissalAdmin)

# Register your models here.
