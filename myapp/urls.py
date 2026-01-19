from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.students, name='student_list'),
    path('register/', views.register, name='create_student'),
    path('edit/<int:id>/', views.edit, name='edit_student'),
    path('delete/<int:id>/', views.delete, name='delete_student'),
    path('show/<int:id>/', views.show, name='show_student'),
    path('add/', views.add_student, name='add_student'),
       
]  