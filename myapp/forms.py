from django import forms
from .models import Blog,Student


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'phone_number']

