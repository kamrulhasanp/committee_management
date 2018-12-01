from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('Committee <int:pk>/event/', views.createEvent, name='create_event'),
    path('<int:pk>/event_detail', views.EventDetailView.as_view(), name='event_detail'),
    path('<int:pk>/New Post', views.creatPost, name='create_post'),
]
