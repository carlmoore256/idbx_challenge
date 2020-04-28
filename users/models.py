from django.db import models
from django.contrib.auth.models import User

# create model for coodinator containing inst. id

class CoordinatorProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   institutional_id = models.IntegerField()

   # return name of profile
   def __str__(self):
       return f'{self.user.username}'
