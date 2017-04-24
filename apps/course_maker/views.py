# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Course

# Create your views here.
def index(request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'course_maker/index.html', context)

def addcourse(request):
    data = {
    'name': request.POST['name'],
    'description': request.POST['description']
    }
    if Course.objects.validate(data, request):
        Course.objects.create(name=name,description=description)
        return redirect('/')
    return redirect('/')

def confirmdelete(request, id):
    context = {
    'course': Course.objects.get(id=id)
    }
    return render(request, 'course_maker/delete.html', context)

def deletecourse(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
