from django.shortcuts import render,get_object_or_404,redirect
from .models import Course
# Create your views here.

def index(request):
    courses = Course.objects
    return render(request, 'index.html',{'courses':courses})

def details(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    return render(request, 'details.html',{'course':course})

def delete(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    course.delete()
    return redirect('/')

