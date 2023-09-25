from django.urls import path
from . import views

urlpatterns = [
    path('view/<int:id>/', views.view, name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('<int:id>', views.view_student, name='view_student'),
    path('', views.index, name='index')
]