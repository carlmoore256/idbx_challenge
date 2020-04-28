from django.db import models
from django.contrib.auth.models import User

# main course class holds course information
class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    language = models.TextField()
    coordinator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
