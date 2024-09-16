from .models import Comment
from django import forms
# from django import formsclass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')