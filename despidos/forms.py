from django import forms
from models import Dismissal

class DismissalForm(forms.ModelForm):

    class Meta:
        model = Dismissal
        fields = ['dismissal_date','comment','workplace']
        widgets = {
                'dismissal_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'datepicker'},)
                }

