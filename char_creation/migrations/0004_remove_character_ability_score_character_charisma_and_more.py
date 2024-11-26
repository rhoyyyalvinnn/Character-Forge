# Generated by Django 5.1.1 on 2024-11-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char_creation', '0003_character_customization_equipment_spell_weapon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='ability_score',
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(default=10),
        ),
    ]