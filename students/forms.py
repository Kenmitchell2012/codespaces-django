from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Student Number'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Field of Study'}),
            'gpa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GPA'}),
        }

