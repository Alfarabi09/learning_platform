from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(User, related_name="classrooms")

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="assignments")
    completed_by = models.ManyToManyField(User, related_name="completed_assignments", blank=True)

class CompletedAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)