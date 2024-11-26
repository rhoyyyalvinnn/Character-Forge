from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'char_class', 'background', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    
    # Set custom choices for the ability scores (example for strength)
    STAT_CHOICES = [(15, '15'), (14, '14'), (13, '13'), (12, '12'), (10, '10'), (8, '8')]
    
    # Define the race and char_class fields as ChoiceField to display select dropdowns
    race = forms.ChoiceField(
        choices=[('dragonborn', 'Dragonborn'),
                 ('dwarf', 'Dwarf'),
                 ('elf', 'Elf'),
                 ('gnome', 'Gnome'),
                 ('half-elf', 'Half-Elf'),
                 ('half-orc', 'Half-Orc'),
                 ('halfling', 'Halfling'),
                 ('human', 'Human'),
                 ('tiefling', 'Tiefling')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    char_class = forms.ChoiceField(
        choices=[('artificer', 'Artificer'),
                 ('barbarian', 'Barbarian'),
                 ('bard', 'Bard'),
                 ('blood_hunter', 'Blood Hunter'),
                 ('cleric', 'Cleric'),
                 ('druid', 'Druid'),
                 ('fighter', 'Fighter'),
                 ('monk', 'Monk'),
                 ('paladin', 'Paladin'),
                 ('ranger', 'Ranger'),
                 ('rogue', 'Rogue'),
                 ('sorcerer', 'Sorcerer'),
                 ('warlock', 'Warlock'),
                 ('wizard', 'Wizard')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Ability scores (stat fields) as ChoiceField
    strength = forms.ChoiceField(choices=STAT_CHOICES, initial=10)
    dexterity = forms.ChoiceField(choices=STAT_CHOICES, initial=10)
    constitution = forms.ChoiceField(choices=STAT_CHOICES, initial=10)
    intelligence = forms.ChoiceField(choices=STAT_CHOICES, initial=10)
    wisdom = forms.ChoiceField(choices=STAT_CHOICES, initial=10)
    charisma = forms.ChoiceField(choices=STAT_CHOICES, initial=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize widgets here if needed, like adding classes
        self.fields['strength'].widget.attrs.update({'class': 'stat-select'})
        self.fields['dexterity'].widget.attrs.update({'class': 'stat-select'})
        self.fields['constitution'].widget.attrs.update({'class': 'stat-select'})
        self.fields['intelligence'].widget.attrs.update({'class': 'stat-select'})
        self.fields['wisdom'].widget.attrs.update({'class': 'stat-select'})
        self.fields['charisma'].widget.attrs.update({'class': 'stat-select'})
