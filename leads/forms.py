from django import forms

# creating forms

class LeadForm(forms.Form):
    # give fields we need
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)