from http.client import responses

from django.contrib import messages
from django_daraja.mpesa.core import MpesaClient
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from rest_framework import status
from rest_framework.decorators import api_view

from application.forms import StudentForm
from application.models import Student, Course
from application.serializers import StudentSerializer, CourseSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    data = Student.objects.all()
    return render(request, 'about.html', {'data': data})

def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = StudentForm()
    return render(request, 'contact.html', {'form': form})


def edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.error(request, 'Student updated successfully!')
            return redirect('about')
        else:
            messages.error(request, 'Please check form details!')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form': form, 'student': student})

def delete(request,id):
    student = get_object_or_404(Student, id=id)

    try:
        student.delete()
        messages.success(request, 'Student successsfully deleted')

    except Exception as e:
        messages.error(request, 'Student not deleted')

    return redirect('about')

@api_view(['GET', 'POST'])
def studentsapi(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def coursesapi(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0704683152'
    amount = 1
    account_reference = 'eMobilis'
    transaction_desc = 'Payment for Web dev'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = client.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)