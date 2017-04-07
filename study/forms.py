# study/forms.py
from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','origin','video_url', 'video_url2', 'text')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'origin' : forms.TextInput(attrs={'class': 'form-control','placeholder': '자료 출처를 입력해주세요.(not required)'}),
            'video_url' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YouTube 영상이 있다면 공유 URL을 입력해주세요.(not required)'}),
            'video_url2' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YouTube 영상이 있다면 공유 URL을 입력해주세요.(not required)'}),
            'text' : forms.Textarea(attrs={'class': 'form-control', 'rows':15}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text' : forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '댓글을 입력해주세요.'}),
        }


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
