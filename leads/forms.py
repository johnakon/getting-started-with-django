from django import forms
from .models import Lead

# creating forms


# model form
class LeadModelForm(forms.ModelForm):
    # create class called meta
    class Meta:
    # info of the form
        model = Lead
        # fields to display as a tuple
        fields = {
            'first_name',
            'last_name',
            'age',
            'agent',
        }


class LeadForm(forms.Form):
    # give fields we need
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)