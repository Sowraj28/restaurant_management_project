from django import forms
from .models import Feedback

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