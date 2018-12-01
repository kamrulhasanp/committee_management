from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic

from .forms import TeacherProfileForm
from users.models import CustomUser


# Create your views here.

@login_required
def update_profile(request):
    if request.method == 'POST':
        teacherProfile = TeacherProfileForm(request.POST, request.FILES, instance=request.user)
        if teacherProfile.is_valid():
            teacherProfile.save()
            return redirect('view_profile', request.user.pk)
        else:
            pass

    else:
        teacherProfile = TeacherProfileForm(instance=request.user)

    return render(request, 'teachers/update_profile.html', {
        'teacherProfile': teacherProfile,
    })


class ProfileDetail(generic.DeleteView):
    template_name = 'teachers/view_profile.html'
    model = CustomUser
