# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewProjectForm, NewModuleForm
from .models import Project, Module, Activity

###

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'home.html'

###

def new_project(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        submission_deadline = request.POST['submission_deadline']
        user = User.objects.first()
        project = Project.objects.create(
                                    name=name,
                                    description=description,
                                    submission_deadline=submission_deadline
                                    )
        return render(request, 'home.html')
    return render(request, 'new_project.html')

##

def project_modules(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'modules.html', {'project': project})

##

def new_module(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        name = request.POST['name']
        submission_deadline = request.POST['submission_deadline']
        description = request.POST['description']
        status = request.POST['status']
        
        user = User.objects.first()
        
        module = Module.objects.create(
                                     name=name,
                                     submission_deadline=submission_deadline,
                                     description=description,
                                     status=status,
                                     project=project,
                                     starter=user
                                     )

        return redirect('project_modules', pk=project.pk)  # TODO: redirect to the created module page

    return render(request, 'new_module.html', {'project': project})

###

def module_activities(request, pk, module_pk):
    module = get_object_or_404(Module, project__pk=pk, pk=module_pk)
    
    
    return render(request, 'module_activities.html', {'module': module})

##

def new_module(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        name = request.POST['name']
        submission_deadline = request.POST['submission_deadline']
        description = request.POST['description']
        status = request.POST['status']
        
        user = User.objects.first()
        
        module = Module.objects.create(
                                       name=name,
                                       submission_deadline=submission_deadline,
                                       description=description,
                                       status=status,
                                       project=project,
                                       starter=user
                                       )
                                       
        return redirect('project_modules', pk=project.pk)  # TODO: redirect to the created module page
    
    return render(request, 'new_module.html', {'project': project})

##

def first_activity(request, pk):
    module = get_object_or_404(Module, pk=pk)
    
    if request.method == 'POST':
        name = request.POST['name']
        submission_deadline = request.POST['submission_deadline']
        description = request.POST['description']
        status = request.POST['status']
        
        user = User.objects.first()
        
        module = Module.objects.create(
                                       name=name,
                                       submission_deadline=submission_deadline,
                                       description=description,
                                       status=status,
                                       module=module,
                                       starter=user
                                       )
    
                                       
        return redirect('project_modules', pk=project.pk)  # TODO: redirect to the created module page
    
    
    return render(request, 'first_activity.html', {'module': module})

####

def last_activity(request, pk):
    module = get_object_or_404(Module, pk=pk)
    
    if request.method == 'POST':
        name = request.POST['name']
        submission_deadline = request.POST['submission_deadline']
        description = request.POST['description']
        status = request.POST['status']
        
        user = User.objects.first()
        
        module = Module.objects.create(
                                       name=name,
                                       submission_deadline=submission_deadline,
                                       description=description,
                                       status=status,
                                       module=module,
                                       starter=user
                                       )
                                       
                                       
        return redirect('project_modules', pk=project.pk)  # TODO: redirect to the created module page
    
    
    return render(request, 'last_activity.html', {'module': module})

###

def new_activity(request, pk):
    module = get_object_or_404(Module, pk=pk)
    
    if request.method == 'POST':
        name = request.POST['name']
        submission_deadline = request.POST['submission_deadline']
        description = request.POST['description']
        status = request.POST['status']
        
        user = User.objects.first()
        
        module = Module.objects.create(
                                       name=name,
                                       submission_deadline=submission_deadline,
                                       description=description,
                                       status=status,
                                       module=module,
                                       starter=user
                                       )
                                       
                                       
        return redirect('project_modules', pk=project.pk)  # TODO: redirect to the created module page
    
    
    return render(request, 'new_activity.html', {'module': module})



