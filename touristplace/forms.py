from allauth.account.forms import SignupForm
from django import forms
from django.forms.widgets import Widget
from django.utils.html import format_html
from .models import Rev

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class RevForm(forms.ModelForm):
    class Meta:
        model = Rev
        fields = ['rating', 'comment']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Search')