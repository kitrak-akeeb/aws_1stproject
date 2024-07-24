from django import forms
from .models import Cars 

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name', 'description', 'manufacturer', 'year', 'image']
    

        labels = {
            'name': 'Car Name *',
            'description': 'Description *',
            'manufacturer': 'Manufacturer *',
            'year': 'Year *',
            'image': 'Image',
        }
        error_messages = {
            'name': {
                'required': 'This field is required.',
            },
            'description': {
                'required': 'This field is required.',
            },
            'manufacturer': {
                'required': 'This field is required.',
            },
            'year': {
                'required': 'This field is required.',
            },
        }