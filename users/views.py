from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         teacherProfile = TeacherProfileForm(request.POST, instance=request.user)
#         if teacherProfile.is_valid():
#             teacherProfile.save()
#             return redirect('view_profile', request.user.slug)
#         else:
#             pass
#
#     else:
#         teacherProfile = TeacherProfileForm(instance=request.user)
#
#     return render(request, 'update_profile.html', {
#         'teacherProfile': teacherProfile,
#     })
#
#
# class ProfileDetail(generic.DeleteView):
#     template_name = 'view_profile.html'
#     model = CustomUser
