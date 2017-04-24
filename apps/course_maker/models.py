# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

# Create your models here.

class CourseManager(models.Manager):
    def validate(self, data, request):
        valid=True
        if len(data['name'])<1:
            messages.error(request, 'name is a required field')
            valid=False
        if len(data['description'])<1:
            messages.error(request, 'description is required')
        return valid

class Course(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
