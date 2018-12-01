from django import forms
from users.models import CustomUser


class TeacherProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    teacherID = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'teacherID', 'designations', 'image',)
