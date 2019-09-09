# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Report
from .models import ReportResponse
from .models import User

# Register your models here.

admin.site.register(Report)
admin.site.register(ReportResponse)
admin.site.register(User)