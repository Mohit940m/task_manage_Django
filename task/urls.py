from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("create/", views.task_create, name="task_create"),
    
    path("<int:task_id>/edit/", views.task_edit, name="task_edit"),
    path("<int:task_id>/delete/",views.task_delete, name="task_delete"),
    path("register/",views.register, name="register"),
    
    path('tasks/<int:task_id>/change_status/', views.change_task_status, name='task_change_status'),
]
