from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
    
    labels = {
        #'id':'ID',
        'full_name':"Full Name",
        'address':'Address',
        'birthplace':'Birthplace',
        'education':'Educatuion',
        'gender':'Gender',
        'date_of_birth':'Date of Birth',
    }
    
    widgets ={
        'address' : forms.TextInput(attrs={'placeholder': 'eg. 8th floor Duong Dinh Nghe str'}),
        'date_of_birth' : forms.DateInput(attrs={'placeholder': 'đd/mm/YYYY'}),
    }