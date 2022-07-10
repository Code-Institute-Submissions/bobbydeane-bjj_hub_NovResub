from django import forms
from .models import Review, Product, Category


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'deane', 'type':'hidden'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}), 
        }

    # Edit products form
class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    # Override init method to make changes to fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        #get a list of tuples of catergory names assoc with their friendly ids
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-50'

