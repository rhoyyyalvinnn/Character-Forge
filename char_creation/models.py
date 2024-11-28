from django.contrib.auth.models import User
from django.db import models

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    char_class = models.CharField(max_length=255) 
    background = models.CharField(max_length=255)
    # Stats as individual fields
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
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
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    spells = models.ManyToManyField(Spell)  # Many-to-many relationship with Spell
    weapons = models.ManyToManyField(Weapon)
    equipments = models.ManyToManyField(Equipment)


    def __str__(self):
        return f"Customization for {self.character.name}"


