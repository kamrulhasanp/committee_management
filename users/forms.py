import re
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[diu|daffodilvarsity]+.edu.bd')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError('Invalid Email format')
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


# class TeacherProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50, required=False)
#     last_name = forms.CharField(max_length=50, required=False)
#     teacherID = forms.IntegerField(max_value=9)
#
#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email', 'teacherID', 'designations')
