from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signinform(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

    def save(self, commit=True):
        User = super(signinform, self).save(commit=False)
        User.email = self.cleaned_data["email"]
        User.first_name = self.cleaned_data["first_name"]
        User.last_name = self.cleaned_data["last_name"]

        if commit:
            User.save()
        return User

    