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
        'image':'Image',
    }

    