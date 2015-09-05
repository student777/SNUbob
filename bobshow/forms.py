from django import forms
from bobshow.models import Bob, Comment, Photo
from django.utils.translation import ugettext_lazy as _


class BobForm(forms.ModelForm):
    class Meta:
        model = Bob
        fields = ('name', 'image', 'place',)
        labels = {
            'name': _('어떤 메뉴를 드셨나요?'),
            'image': _('사진'),
            'place': _('어디서 식사하셨나요?'),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        name = name.replace(" ", "")
        if name:
            if len(name) < 3:
                raise forms.ValidationError("3글자 이상 입력하세요")
        return name


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'star')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', )
