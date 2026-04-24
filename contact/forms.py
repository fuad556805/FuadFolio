from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Jane Doe',
                'autocomplete': 'name',
                'maxlength': 100,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'autocomplete': 'email',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me a bit about your project or idea…',
                'rows': 5,
            }),
        }
