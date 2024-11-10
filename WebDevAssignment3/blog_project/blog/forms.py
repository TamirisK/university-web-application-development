from django import forms
from django.contrib.auth.models import User
from .models import Post, Category, Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'image', 'categories'] 

class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'image']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.all() 

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }

