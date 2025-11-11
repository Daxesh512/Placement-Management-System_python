from __future__ import unicode_literals
import os
from django.db import models
from django.urls import reverse
import datetime
from company.models import Job_desc

# File upload helper
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.s_username, ext)
    return os.path.join('documents/', filename)


class StudentDB(models.Model):
    COURSE = (
        ('BTECH', 'bachelors'),
        ('MTECH', 'masters'),
        ('PHD', 'philospher'),
    )
    BRANCH = (
        ('CS', 'computer_science'),
        ('ME', 'mechanical'),
        ('EE', 'electrical'),
    )
    s_username = models.CharField(max_length=250, default='')
    s_name = models.CharField(max_length=250, blank=True)
    s_password = models.CharField(max_length=250, blank=True)
    s_confirm_password = models.CharField(max_length=250, blank=True)
    dob = models.DateField()
    emailid = models.EmailField(blank=True)
    branch = models.CharField(max_length=10, choices=BRANCH, default='CS')
    course = models.CharField(max_length=5, choices=COURSE, default='BTECH')
    s_verified = models.BooleanField(default=False, blank=True)
    s_verification = models.IntegerField(default=0, blank=True)
    contactno = models.CharField(max_length=20, blank=True)
    resume = models.FileField(upload_to=content_file_name, blank=True)

    def __str__(self):
        return str(self.s_username)


class Edit_Details(models.Model):
    s_name = models.CharField(max_length=250, blank=True, null=True)
    emailid = models.EmailField(blank=True)
    qualification = models.CharField(max_length=250, blank=True, null=True)
    resume = models.FileField(upload_to="documents/", blank=True)

    def __str__(self):
        return self.s_name


class Notifications(models.Model):
    jobid = models.ForeignKey(Job_desc, on_delete=models.CASCADE, null=True)
    n_text = models.CharField(max_length=250, null=True)
    old = models.BooleanField(default=True)
    stdid = models.ForeignKey(StudentDB, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.n_text)


class AppliedJob(models.Model):
    jobid = models.ForeignKey(Job_desc, on_delete=models.CASCADE, null=True)
    stdid = models.ForeignKey(StudentDB, on_delete=models.CASCADE, null=True)
    applied = models.BooleanField(default=False)
    got_offer = models.CharField(max_length=250, default="No")

    def __str__(self):
        return str(self.got_offer)


# Example of a future extension:
# class Course(models.Model):
#     course_name = models.CharField(max_length=100)
#     shorthand = models.CharField(max_length=5)
