from django.contrib import admin

from .models import Member, Leader, SlideView
from .models import Committee
from .forms import LeaderForm, MemberForm


# Register your models here.
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'leaderNumber', 'memberNumber', 'created_On', 'updated_On']
    search_fields = ['__str__', 'name']
    fields = [('Leader', 'teacher')]

    class Meta:
        model = Committee


admin.site.register(Committee, CommitteeAdmin)


class CommitteeLeaderAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Leader


admin.site.register(Leader, CommitteeLeaderAdmin)


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Member


admin.site.register(Member, CommitteeMemberAdmin)


class SlideViewAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']

    class Meta:
        model = SlideView


admin.site.register(SlideView, SlideViewAdmin)

#
# class AdminTeachers(admin.ModelAdmin):
#     list_display = ['__str__', 'name', 'teacherId', 'designation', 'created_at', 'updated_at']
#     search_fields = ['__str__', 'name']
#
#
# admin.site.register(AdminTeachers)
# # admin.site.register(models.Leader)
# # admin.site.register(models.Member)
