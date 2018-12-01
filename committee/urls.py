from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommitteeListView.as_view(), name='committee_list'),
    path('new/', views.CommitteeCreateView.as_view(), name='new_committee'),
    path('<int:pk>/detail/', views.CommitteeDetailView.as_view(), name='committee_detail'),
    path('<int:pk>/new Slide/', views.makeSliderView, name='addSlide'),

    path('<int:pk>/select_leader/', views.select_leader, name='select_leader'),
    path('<int:pk>/select_member/', views.select_member, name='select_member'),

]
