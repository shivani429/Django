from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import *
from demoapp.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from django.views.generic import ListView,View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

# from .models import Blog

# def mul(request):
#     if request.method =='POST':
#         val1 = int(request.POST['fn'])
#         val2 = int(request.POST['sn'])
#         res = val1 * val2
#     return render(request,'result.html',{'result':res})
    

def home(request):
    return render(request,'home.html',{'name':'Django'})

def home(request):
    post = Blog.objects.all()
    return render(request,'home.html',{'post':post})

# def indexView(request):
#     return render(request,'index.html')

# def dashboardView(request):
#     return render(request,'dashboard.html')

def home(request):
       return render(request, 'home.html')   

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponse(request,'login.html',{'form':form})
#     else:
#         return render(request,'login1.html')
       

# Student Functions
def student_list(request):
    student_list = Student.objects.all()
    d = {'student_list': student_list}
    return render(request,'index.html',d)
    
def delete_student(request,id):
    stu = Student.objects.get(id=id)
    stu.delete()
    return redirect('student_list')

def update_student(request, id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':        
        Name = request.POST.get('name')
        roll_no_=request.POST.get('Roll_no')
        class_no_ = request.POST.get('class_no')
        address = request.POST.get('Address')
        print(Name)
        print(roll_no_)
        print(class_no_)
        print(address)
        stu.Roll_no = roll_no_
        stu.name = Name
        stu.class_no = class_no_
        stu.Address = address
        stu.save()
        return redirect('student_list')
    else:
    
        d = {'stu': stu}
        return render(request,'update.html',d)

def add_student(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        roll_no_=request.POST.get('Roll_no')
        class_no_ = request.POST.get('class_no')
        address = request.POST.get('Address')
        print(Name)
        print(roll_no_)
        print(class_no_)
        print(address)
        Student.objects.create(Roll_no=roll_no_,name=Name,class_no=class_no_,Address=address)
        return redirect('student_list')
    else:
        form = StudentForm()
        return render(request, 'update.html', {"form": form})


# Employee Functions
def employee_list(request):
    employee_list = Employee.objects.all()
    e = {'employee_list':employee_list}
    return render(request,'employee.html', e)

def delete_employee(request,id):
    em = Employee.objects.get(id=id).delete()
    return redirect('employee_list')

def edit_employee(request,id):
    em = Employee.objects.get(id=id)
    if request.method=='POST':
        eid_ = request.POST.get('eid')
        ename_ = request.POST.get('ename')
        ephn_ = request.POST.get('ephn')
        esalary_ = request.POST.get('esalary')
        print('eid_')
        print('ename_')
        print('ephn_')
        print('esalary_')
        em.eid = eid_
        em.ename = ename_
        em.ephn = ephn_
        em.esalary = esalary_
        em.save()
        return redirect('employee_list')
    else:
        e = {'em':em}
        return render(request,'edit.html',e)

def add_employee(request):
    if request.method=='POST':
        eid_ = request.POST.get('eid')
        ename_ = request.POST.get('ename')
        ephn_ = request.POST.get('ephn')
        esalary_ = request.POST.get('esalary')
        print('eid_')
        print('ename_')
        print('ephn_')
        print('esalary_')
        Employee.objects.create(eid = eid_, ename = ename_, ephn = ephn_, esalary = esalary_)
        return redirect('employee_list')
    else:
        return render(request,'edit.html')
    
#django CRUD
def create_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        form = Details.objects.create(name = name, age = age, address = address) 
        form.save()
        return redirect('retrieve')
    return render(request,'details.html')
         
def retrieve(request):
    form = Details.objects.all()
    return render(request,'retrieve.html',{'form':form})  

def update1(request,id):
    object = Details.objects.get(id=id)
    if request.method == 'POST':
        if object:
            object.name = request.POST['name']
            object.age = request.POST['age']
            object.address = request.POST['address']
            object.save()
        return redirect('retrieve')
    return render(request,'editt.html',{'object':object})
    
def delete1(request,id):
    object = Details.objects.get(id=id)
    object.delete()
    return redirect('retrieve')   

#task1 using foreign key
def salary_list(request):
    salary_list = EmployeeSalary.objects.all()
    s = {'salary_list':salary_list}
    return render(request,'salary.html',s)

def deletesalary(request,id):
    salary = EmployeeSalary.objects.get(id=id)
    salary.delete()
    return redirect('salary_list')

def update_salary(request,id):
    employee_list = EmployeeSalary.objects.get(id=id)
    emp_list = Employee.objects.all()
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee_ = request.POST.get('employee')
        employee_list.basic = basic_
        employee_list.hra = hra_
        employee_list.special_allowance = special_allowance_
        employee_list.pf_deduction = pf_deduction_
        employee_list.income_tax = income_tax_
        employee_list.proffesional_tax = proffesional_tax_
        employee_list.convenience = convenience_
        employee_list.lta = lta_
        em_name = Employee.objects.get(id = int(employee_))
        employee_list.employee = em_name
        employee_list.save()
        return redirect('salary_list')
    else:
        a = {'salary':employee_list, 'employee_list': emp_list }
        return render(request,'update1.html',a)

def addcontent(request):
    employee_list = Employee.objects.all()
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee = request.POST.get('employee')
        EmployeeSalary.objects.create(basic=basic_, hra=hra_, 
        special_allowance=special_allowance_, pf_deduction=pf_deduction_, 
        income_tax=income_tax_, proffesional_tax=proffesional_tax_, convenience=convenience_, 
        lta=lta_,employee_id=employee)
        return redirect('salary_list')
    else:
        return render(request,'update1.html',{'employee_list':employee_list})

#Authentication 
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Incorrect Username or Password')
        return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user')
            messages.success(request,'Account created for '+ 'user') 
            return redirect('login')

    context = {'form':form}
    return render(request,'register1.html',context)

#javascript validation
def insert(request):
    return render(request,'insert.html')

#AJAX example
# def profile(request):
#     return render(request,'profile.html')

# def getprofile(request):
#     profile = Profile.objects.all()
#     return JsonResponse({'profile':list(profile.values())})

# def post(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         bio = request.POST['bio']
#         new_user = Profile(name=name, email=email, bio=bio)
#         new_user.save()
#         return HttpResponse('new data created successfully')

#AJAX example
def photo_view(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data["name"] = form.cleaned_data.get("name")
            data["status"] = 'ok'
            return JsonResponse(data)
    context = {'form':form}
    return render(request,'main.html',context)

#AJAX example
def hello(request):
    return render(request,'hello.html')

class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('hello')
    def form_valid(self,form):
        valid = super().form_valid(form)
        login(self.request,self.object)
        return valid
def validate_username(request):
    username = request.GET.get('username',None)
    response = {
        'is_taken':User.objects.filter(username__iexact = username).exists()
    }
    return JsonResponse(response)
    
#CRUD using AJAX
class crudview(ListView):
    model = CrudUser
    template_name = "crud.html"
    context_object_name = 'users'

class CreateCrudUser(View):
    def get(self,request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age',None)
        obj = CrudUser.objects.create(name=name1, address = address1, age = age1)
        user = {'id':obj.id, 'name':obj.name, 'address':obj.address, 'age':obj.age}
        data = {'user':user}
        return JsonResponse(data)
    
class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
#QuizForm    
def hom(request):
    if request.method == "POST":
        questions=QuizModel.objects.all()
        score=0
        correct=0
        wrong=0
        total=0
        for q in questions:
            total+=1
            if q.ans == request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        context = {
            'score':f'{score}/{total}',
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'res.html',context)
    else:
        questions = QuizModel.objects.all()
        context = {'questions':questions}
        return render(request,'hom.html',context)  
    
def addquestion(request):
    form = QuizModelForm()
    if request.method == 'POST':
        form = QuizModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addquestion')
    context={'form':form}
    return render(request,'addqns.html',context)

#task3
def email(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('empdata')
            except:
                pass
    else:
        form = EmpForm()
    return render(request, 'email.html', {"form": form})


def empdata(request):
    object = Emp.objects.all()
    return render(request, 'empdata.html', {'object': object})


def update_data(request, id):
    object = Emp.objects.get(id=id)
    if request.POST:
        if object:
            object.Empcode = request.POST['Empcode']
            object.Name =request.POST['Name']
            object.DOBirth =request.POST['DOBirth']
            object.DOJoining = request.POST['DOJoining']
            object.DOAnniversary = request.POST['DOAnniversary']
            object.Email = request.POST['Email']
            object.save()
        return redirect('empdata')
    return render(request, 'editdata.html', {'object': object})


def delete_data(request, id):
    object = Emp.objects.get(id=id)
    object.delete()
    return redirect('empdata')

def data(request):
    return redirect('edata')

def edata(request):
    today_date = datetime.today().date()
    birthdays = Emp.objects.filter(DOBirth__day=today_date.day,DOBirth__month=today_date.month)
    joining = Emp.objects.filter(DOJoining__day=today_date.day,DOJoining__month=today_date.month)
    annversary = Emp.objects.filter(DOAnniversary__day=today_date.day,DOAnniversary__month=today_date.month)
    return render(request, 'data.html',{'birthdays':birthdays, 'joining':joining, 'annversary':annversary})

def query(request):
    return redirect('mail')

def mail(request):
    return render(request,'message.html')

#Django Ajax 
def blog(request):
    context_dict = {}

    # Get all blogs titles in ascending order
    blogs = Blog.objects.order_by('title')
    context_dict['blogs'] = blogs

    return render(request, "likes.html", context=context_dict)
    
def add_new_blog_ajax(request):
    if request.method == 'GET':
        blog_title = request.GET.get('blog_title')

        if blog_title:
            Blog.objects.create(title=blog_title, likes=0)
            return JsonResponse({'status': "created"})
        else:
            return JsonResponse({'status': "failed"})   
        
def add_likes_ajax(request):
    if request.method == 'GET':
        blog_id = request.GET.get('blog_id')
        likes = 0
        if blog_id:
            blog = Blog.objects.get(id=int(blog_id))
            if blog:
                likes = blog.likes + 1
                blog.likes = likes
                blog.save()
        return JsonResponse({'total_likes': likes})
    
def delete_blog_ajax(request):
    if request.method == 'GET':
        blog_id = request.GET.get('blog_id')

        if blog_id:
            blog = Blog.objects.get(id=int(blog_id))
            if blog:
                blog.delete()
                return JsonResponse({'status': "deleted"})
            else:
                return JsonResponse({'status': "error"})