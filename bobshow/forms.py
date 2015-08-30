from django import forms
from bobshow.models import Bob, Comment


class BobForm(forms.ModelForm):
    class Meta:
        model = Bob
        fields = ('name', 'content', 'image', 'place', 'star')

    def clean_name(self):
        name = self.cleaned_data['name']
        name = name.replace(" ", "")
        if name:
            if len(name) < 3:
                raise forms.ValidationError("3글자 이상 입력하세요")
        return name

    def clean_star(self):
        star = self.cleaned_data['star']
        if star < 0 or star > 5:
            raise forms.ValidationError('0~5 사이의 정수를 입력하세요')
        return star



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'star' )



