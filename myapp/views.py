from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models  import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('login')
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        user_name=request.POST.get('username')
        password_1=request.POST.get('password1')
        password_2=request.POST.get('password2')
        email = request.POST.get('email')
        if password_1==password_2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name, first_name=first_name ,last_name=last_name ,password=password_1, email=email)
                user.save()
                print('user created')
                return redirect('login')

        else:
                messages.info(request,'passwords doesnt match')
                return redirect('register')

    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
@login_required
def home(request):
    task=Task.objects.filter(user=request.user)
    return render(request,'home.html',{'tasks':task})
@login_required
def add(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)#not storing to db
            task.user=request.user
            task.save()
            return redirect('home')
    else:
        form=TaskForm()
    return render(request, 'add.html', {'form': form})

@login_required
def update(request,id):
    tasks = get_object_or_404(Task, id=id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TaskForm(instance=tasks)

    return render(request,'update.html',{'form':form , 'tasks':tasks})
@login_required
def delete(request,id):
    tasks=get_object_or_404(Task,id=id)
    tasks.delete()
    return redirect('home')
