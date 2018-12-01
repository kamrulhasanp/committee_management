from django.contrib import admin
from .models import Event, Post


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['eventName', 'description', 'image']

    class Meta:
        model = Event


admin.site.register(Event, EventAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
