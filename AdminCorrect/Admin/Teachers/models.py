from django.db import models
from Accounts.models import User
# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=50)
    startDate = models.DateField()
    EndDate = models.DateField()
    certificate = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} start on {self.startDate}, end on {self.EndDate}"
    

class CurrentCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"is_student": True})
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Available courses are {self.course}"