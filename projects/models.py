# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    submission_deadline = models.DateField(auto_now_add=False)
    start_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
    
    def get_activities_count(self):
        return Activity.objects.filter(task__project=self).count()
    
    def get_last_activity(self):
        return Activity.objects.filter(task__project=self).order_by('-created_at').first()


class Module(models.Model):
    name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=4000)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    submission_deadline = models.DateField(auto_now_add=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='modules')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modules')
    work_day_started = models.BooleanField(default=False)
    
    def __str__(self):
        return self.subject

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=4000)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='activities')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20)
    submission_deadline = models.DateTimeField(auto_now_add=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
    
    
    def __str__(self):
        truncated_description = Truncator(self.description)
        return truncated_description.chars(30)

class Note(models.Model):
    description = models.TextField(max_length=4000)
    def __str__(self):
        truncated_description = Truncator(self.description)
        return truncated_description.chars(30)
