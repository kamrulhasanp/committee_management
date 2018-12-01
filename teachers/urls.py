from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_profile, name='update_profile'),
    path('<int:pk>', views.ProfileDetail.as_view(), name='view_profile'),

]
