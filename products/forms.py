from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'deane', 'type':'hidden'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            #'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder':' product name', 'id': 'prod'}),
        }

