from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm, StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'index.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})

def blog_update(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form})

def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog_confirm_delete.html', {'blog': blog})

def student_list(request):
    student_list = Student.objects.all()
    return render(request , 'student_list.html',context={'student_list':student_list})

# def student_create(request):
#     form = StudentForm()
#     return render(request,'student_create.html',{"form" : form})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Student_list')
        else:
            print(form.errors) 
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {'form': form})

def student_update(request, id):
    stu_obj = Student.objects.get(id = id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu_obj)
        if form.is_valid():
            form.save()
            return redirect('Student_list')
        else:
            print(form.errors) 
    else:
        form = StudentForm(instance=stu_obj)
    return render(request, 'student_create.html', {'form': form})