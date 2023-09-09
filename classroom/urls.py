from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classroom/<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('classrooms/', views.ClassroomListView.as_view(), name='classroom_list'),
    path('classrooms/add/', views.ClassroomCreateView.as_view(), name='classroom_add'),
    path('classrooms/<int:pk>/', views.ClassroomDetailView.as_view(), name='classroom_detail'),
    path('classrooms/<int:pk>/edit/', views.ClassroomUpdateView.as_view(), name='classroom_edit'),
    
    # Assignment URLs
    path('assignments/', views.AssignmentListView.as_view(), name='assignments_list'),  
    path('assignments/add/', views.AssignmentCreateView.as_view(), name='assignment_add'),
    path('assignments/<int:pk>/', views.AssignmentDetailView.as_view(), name='assignment_detail'),
    path('assignments/<int:pk>/edit/', views.AssignmentUpdateView.as_view(), name='assignment_edit'),
    path('assignments/complete/<int:assignment_id>/', views.mark_assignment_completed, name='mark_completed'),
]