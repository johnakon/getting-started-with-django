from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# import abstract user
from django.contrib.auth.models import AbstractUser

# custom User model
# inherit from AbstractUser
class User(AbstractUser):
    pass

class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # every lead will have its own agaent
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # deleting an agent deletes a lead

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# an agent to manage a lead
class Agent(models.Model):
    # if a user is deleted, their agent is also deleted
    # one agent for every one user-> OneToOneField --linked to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # return string definition
    def __str__(self):
        return self.user.email





