from django import forms
from .models import Feedback
from .models import contact


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['comment']
        widgets={
            'comment':forms.Textarea(attrs={
                'placeholder':'leave Your Feedback Here...',
                'rows':4,
                'cols':40
            })
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Your Name','class':'form-input'}),
            'email':forms.EmailInput(attrs={'placeholder':'Your Email','class':'form=input'}),
        }