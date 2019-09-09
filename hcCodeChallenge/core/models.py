# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User (models.Model):
    
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()

class Report (models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors_set')
    message = models.TextField()
    supervisors = models.ManyToManyField(User, related_name='supervisors_set')

class ReportResponse (models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    report = models.ForeignKey(Report, related_name='reports_set')