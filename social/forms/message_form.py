from django import forms
from social.models.message import Message


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000)

    image = forms.ImageField(required=False)

    class Meta:
        model = Message
        fields = ['body', 'image']