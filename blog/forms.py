# blog/forms.py

from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tag_input = forms.CharField(
        label='Tags',
        help_text='태그를 입력하세요. (최대 5개, 띄어쓰기로 구분)',
        widget=forms.TextInput(attrs={'placeholder': '#힙합 #사랑 #감성힙합'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'link', 'tag_input']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # 기존 tags 초기값 설정
            tags = self.instance.tags.all()
            tag_str = ' '.join(f'{tag.name}' for tag in tags)
            self.fields['tag_input'].initial = tag_str

    def clean_tag_input(self):
        tag_input = self.cleaned_data['tag_input']
        tags = [tag for tag in tag_input.strip().split() if tag]
        if len(tags) > 5:
            raise forms.ValidationError('태그는 최대 5개까지만 입력할 수 있습니다.')
        return tags