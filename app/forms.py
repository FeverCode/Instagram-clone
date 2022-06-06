from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#......
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments','name','likes',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

# Create your forms here.


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['email'].initial = 'e@email.com'
