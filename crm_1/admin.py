from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register([UserProfile, Role, CustomerInfo, Student, CustomerFollowUp, Course, ClassList, CourseRecord,
                     StudyRecord, Branch, Menus])
