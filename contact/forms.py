from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

   name = forms.CharField(
         label="Your Name"
    )
    email = forms.EmailField(
        label="Email Address"
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 8,
        })
    )

    class Meta:
        fields = ['name', 'email', 'message']