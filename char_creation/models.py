from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    char_class = models.CharField(max_length=255)  # 'class' is a reserved keyword in Python
    background = models.CharField(max_length=255)
    ability_score = models.IntegerField()

    def __str__(self):
        return self.name
    
class Spell(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    effect = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    effect = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Customization(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE, null=True, blank=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Customization for {self.character.name}"

