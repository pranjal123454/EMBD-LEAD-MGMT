from django import forms
from .models import Lead,Upcoming_Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields=(
            'first_name',
            'last_name',
            'requirement',
            'country',
            'service_id',
            'service_type',
            'service_tenure',
            'service_active',
            'age',
            'agent',
        )


class Upcoming_LeadModelForm(forms.ModelForm):
    class Meta:
        model=Upcoming_Lead
        fields=(
            'name',
            'email',
            'phone_number',
            'country',
            'lead_description'
        )





class LeadForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    requirement=forms.CharField()
    country=forms.CharField()
    service_id=forms.CharField()
    service_type=forms.CharField()
    service_tenure=forms.CharField()
    service_active=forms.CharField()
    age=forms.IntegerField(min_value=0)

class Upcoming_LeadForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    country=forms.CharField()
    lead_description = forms.CharField()    