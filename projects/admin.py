# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Module, Activity, Note
# Register your models here.
admin.site.register(Project)
admin.site.register(Module)
admin.site.register(Activity)
admin.site.register(Note)
