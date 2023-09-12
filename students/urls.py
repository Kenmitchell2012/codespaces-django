from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.view_student, name='view_student'),
    path('', views.index, name='index')
]