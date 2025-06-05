from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from . import models
from ToDo_Django.models import todoo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

def signup(request):
    if request.method=='POST':
        name=request.POST.get('usrname')
        email=request.POST.get('mail')
        pswd=request.POST.get('pwd')
        print(name,email,pswd)

        my_user = User.objects.create_user(name, email, pswd)
        my_user.save()

        return redirect ('/loginn')
    return render(request, 'signup.html')

def loginn(request):
    if request.method=='POST':
        name=request.POST.get('usrname')
        pswd=request.POST.get('pwd')

        print(name,pswd)
        
        userr = authenticate(request, username=name, password=pswd)
        if userr is not None:
            login(request, userr)
            return redirect('/todopage')
        else:
            return redirect('/loginn')
    return render(request, 'loginn.html')


@login_required(login_url='/loginn')
def todopage(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        print(task)

        obj = models.todoo(task=task, user=request.user)
        obj.save()

    res = models.todoo.objects.filter(user=request.user).order_by('date')
    return render(request, 'todopage.html', {'res': res})


def logout_view(request):
    logout(request)
    return redirect('/loginn')

@login_required(login_url='/loginn')
def edit_todo(request, srno):
    if request.method == 'POST':
        task = request.POST.get('task')
        print(task)

        obj = models.todoo.objects.get(srno=srno)
        obj.task = task
        obj.save()
        return redirect('/todopage')
    obj = models.todoo.objects.get(srno=srno)
    # res = models.todoo.objects.filter(user=request.user).order_by('date')
    return render(request, 'edit_todo.html', {'obj':obj})

@login_required(login_url='/loginn')
def delete_todo(request, srno):
    obj = models.todoo.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')