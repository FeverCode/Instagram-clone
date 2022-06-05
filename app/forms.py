from django import forms
from .models import Image
#......
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','name','likes',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
