from django import forms
from .models import Client, Comment, CommentReply


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['story', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['reply', ]


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['reply', ]
