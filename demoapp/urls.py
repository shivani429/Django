from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from demoapp.views import *
urlpatterns = [

    # path('',views.indexView,name='home'),
    # path('dashboard/',views.dashboardView,name='dashboard_url'),

    path('home', views.home, name='home'),
    path('login/', views.login, name='login'),

    
    # Student Functions
    path('student_list', views.student_list, name='student_list'),
    path('delete_student/<int:id>/', views.delete_student,name='delete_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('add_student', views.add_student, name='add_student'),
   

    # Employee Functions
    path('employee_list', views.employee_list, name='employee_list'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('edit_employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
    
    #django CRUD
    path('create_data', views.create_data, name= 'create_data'),
    path('retrieve', views.retrieve, name = 'retrieve'),
    path('update1/<int:id>', views.update1, name = 'update1'),
    path('delete1/<int:id>', views.delete1, name = 'delete1'),

    
    #task1 using foreign key
    path('salary',views.salary_list, name='salary_list'),
    path('deletesalary/<int:id>/', views.deletesalary, name='deletesalary'),
    path('update_salary/<int:id>/', views.update_salary, name='update_salary'),
    path('addcontent', views.addcontent, name='addcontent'),

    #Authentication 
    path('login', views.loginpage, name='login'),
    path('register1', views.registerpage, name='register1'),
    path('logout',views.logoutuser, name='logout'),

    #javascript validation
    path('insert', views.insert, name='insert'),
    
    #AJAX example    
    # path('profile', views.profile, name='profile'),
    # path('getprofile', views.getprofile, name='getprofile'),
    # path('post', views.post, name='post'),
    
    #AJAX example    
    path('photo', views.photo_view, name='photo'),

    #CRUD using AJAX
    path('crud', views.crudview.as_view(), name='crudview'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),

    #QuizForm   
    path('hom', views.hom, name='hom'),
    path('addquestion', views.addquestion, name='addquestion'),
    
    #task3    
    path('email', views.email, name='email'),
    path('empdata', views.empdata, name='empdata'),
    path('update_data/<int:id>', views.update_data, name='update_data'),
    path('delete_data/<int:id>', views.delete_data, name='delete_data'),
    path('edata', views.edata, name='edata'),
    path('mail', views.mail, name='mail'),
    
    #Django Ajax
    path('blog', views.blog, name = 'blog'),
    path('add_new_blog_ajax/', views.add_new_blog_ajax, name='add_new_blog_ajax'),
    path('add_likes_ajax/', views.add_likes_ajax, name='add_likes_ajax'),
    path('delete_blog_ajax/', views.delete_blog_ajax, name='delete_blog_ajax'),
  
]