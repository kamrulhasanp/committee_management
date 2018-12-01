from django import forms

from users.models import CustomUser
from .models import Committee, Member, Leader, SlideView
from django.forms import formset_factory


class CommitteeForm(forms.ModelForm):
    descriptions = forms.Textarea()

    class Meta:
        model = Committee
        fields = ('name', 'descriptions', 'leaderNumber', 'memberNumber',)


class LeaderForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(CustomUser.objects.all(), label='Leader')

    class Meta:
        model = Leader
        fields = ('teacher', 'committee')


class MemberForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(CustomUser.objects.all(), label='Member')

    class Meta:
        model = Member
        fields = ('teacher', 'committee')


class SliderForm(forms.ModelForm):
    class Meta:
        model = SlideView
        fields = ('title', 'description', 'image', 'committee')
