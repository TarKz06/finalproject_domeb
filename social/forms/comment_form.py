from django import forms
from social.models.comment import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        }))

    class Meta:
        model = Comment
        fields = ['comment']