from django.http import HttpResponse
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Student
from .camera import run_camera

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('rollno')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        try:
            Student.objects.create(
                name=name,
                student_id=student_id,
                email=email,
                image=image
            )
            return redirect('home')
        except IntegrityError:
            return render(request, 'register.html', {
        'error': 'Student ID already exists'
    })

    return render(request, 'register.html')
def open_camera(request):
    run_camera()
    return HttpResponse("camera closed")

