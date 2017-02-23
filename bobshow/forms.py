from django import forms
from bobshow.models import Comment, Image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'star')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
