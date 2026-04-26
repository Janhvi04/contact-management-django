from django import forms 
from .models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["first_name","last_name","address","email","phone_no"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email