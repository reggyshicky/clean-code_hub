from django.contrib import admin
from .models import CurrentCourses, Courses
# Register your models here.
admin.site.register(CurrentCourses)
admin.site.register(Courses)