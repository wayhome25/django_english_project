# study/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','origin','video_url', 'video_url2', 'text')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'origin' : forms.TextInput(attrs={'class': 'form-control','placeholder': '자료 출처를 입력해주세요.(not required)'}),
            'video_url' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YouTube 영상이 있다면 URL을 입력해주세요.(not required)'}),
            'video_url2' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YouTube 영상이 있다면 URL을 입력해주세요.(not required)'}),
            'text' : forms.Textarea(attrs={'class': 'form-control', 'rows':15}),
        }
