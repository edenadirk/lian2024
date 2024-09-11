from django import forms
from .models import Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'id_location',
        'placeholder': 'location...',
    }))

    class Meta:
        model = Profile
        fields = [
            'name',
            'date_of_birth',
            'location',
            'bio',
        ]

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    photo = forms.ImageField(required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'id_location',
        'placeholder': 'location...',
    }))

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'phonenumber',
            'photo',
            'location',
            'category',
            'post_type',
        ]
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')