from django.contrib import admin
from .models import Character, Spell, Weapon, Equipment, Customization

# Register your models here.
admin.site.register(Character)
admin.site.register(Spell)
admin.site.register(Weapon)
admin.site.register(Equipment)
admin.site.register(Customization)