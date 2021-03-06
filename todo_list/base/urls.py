from django.contrib.auth import views
from django.urls import path
from .views import *
from base import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('open_lms/', OpenLms, name='OpenLms'),
    
    path('courses/',Courses.as_view, name='Courses'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
