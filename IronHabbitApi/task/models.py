
from enum import Enum  

from django.db import models
# from django.db.models import
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

# ResetState = Enum('Daily'=1, 'Weekly'=2, 'Monthly'=3)

class ResetState(Enum):
    Daily = 1
    Weekly = 2
    Monthly = 3

class Project(models.Model):
    name = models.CharField(max_length=255)
    # TODO(biniu) change to unlimited length
    description = models.TextField(blank=True)

    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=255)
    # TODO(biniu) change to unlimited length
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=0)
    estimation = models.DateTimeField(default=0)

    # tags = ???

    difficulty = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    priority = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    experience = models.IntegerField()

class Habbit(Task):
    reset = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )

    positive_streak = models.IntegerField()
    negative_streak = models.IntegerField()

class Dailies(Task):
    pass

class DailiesDoneList(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField()
    dailies = models.ForeignKey(Dailies, on_delete=models.CASCADE)
