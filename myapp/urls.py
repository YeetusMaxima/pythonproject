from django.urls import path
from . import views


urlpatterns = [

    # path('home/', views.blog, name = 'blog'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/<int:id>/edit/', views.blog_update, name='blog_update'),
    path('blog/<int:id>/delete/', views.blog_delete, name='blog_delete'),
    path('', views.home, name='home'),  
    path('student_list/', views.student_list , name = "Student_list"),
    path('student_create/' , views.student_create , name = "Student_create"),
    path('student_update/<int:id>/', views.student_update,name = "student_update")
    
    
]
