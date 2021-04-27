from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
