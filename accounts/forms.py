"""import required modules."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Signup."""

    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        """Meta info."""

        model = User
        fields = ('username', 'email', 'password1', 'password2')
