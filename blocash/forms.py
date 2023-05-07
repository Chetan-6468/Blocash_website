from django import forms

class form_dummy(forms.Form):
    name = forms.CharField(max_length=56,required=True)
