from django import forms
from .models import Event, Post


class EventForm(forms.ModelForm):
    description = forms.Textarea()

    class Meta:
        model = Event
        fields = ('eventName', 'description', 'image',)


class PostForm(forms.ModelForm):
    post = forms.Textarea()

    class Meta:
        model = Post
        fields = ('post',)
