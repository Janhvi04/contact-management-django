from django import forms 
from .models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["first_name","last_name","address","email","phone_no"]