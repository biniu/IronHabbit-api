from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hero(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    expirience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    # dynamic stats
    max_hp = models.IntegerField(default=10)
    current_hp = models.IntegerField(default=10)

    max_mana = models.IntegerField(default=10)
    current_mana = models.IntegerField(default=10)

    max_stamina = models.IntegerField(default=10)
    current_stamina = models.IntegerField(default=10)

    # basic stats
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)