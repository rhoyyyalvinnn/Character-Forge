from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from .models import Character, Spell, Weapon, Equipment, Customization
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.template.loader import get_template
import weasyprint

# Create your views here.
def home(request):
    user = request.user

    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, "session/homepage.html", context)

def signout(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    user = request.user
    characters = Character.objects.filter(user=user)  # Get characters for the logged-in user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'characters': characters,  # Pass the characters to the template
    }
    return render(request, "session/profile.html", context)




def actgamerules(request):
    return render(request, "session/actgamerules.html")

def actcommunity(request):
    return render(request, "session/actcommunity.html")

def actforum(request):
    return render(request, "session/actforum.html")

def actcompendium(request):
    return render(request, 'session/actcompendium/actcompendium.html')

def actwiki_spells_artificer(request):
    return render(request, 'session/actcompendium/actspells/actartificer_spell.html')

def actwiki_spells_bard(request):
    return render(request, 'session/actcompendium/actspells/actbard_spell.html')

def actwiki_spells_cleric(request):
    return render(request, 'session/actcompendium/actspells/actcleric_spell.html')

def actwiki_spells_druid(request):
    return render(request, 'session/actcompendium/actspells/actdruid_spell.html')

def actwiki_spells_paladin(request):
    return render(request, 'session/actcompendium/actspells/actpaladin_spell.html')

def actwiki_spells_ranger(request):
    return render(request, 'session/actcompendium/actspells/actranger_spell.html')

def actwiki_spells_sorcerer(request):
    return render(request, 'session/actcompendium/actspells/actsorcerer_spell.html')

def actwiki_spells_warlock(request):
    return render(request, 'session/actcompendium/actspells/actwarlock_spell.html')

def actwiki_spells_wizard(request):
    return render(request, 'session/actcompendium/actspells/actwizard_spell.html')

def actwiki_lineages_dragonborn(request):
    return render(request, 'session/actcompendium/lineages/dragonborn.html')

def actwiki_lineages_dwarf(request):
    return render(request, 'session/actcompendium/lineages/dwarf.html')

def actwiki_lineages_elf(request):
    return render(request, 'session/actcompendium/lineages/elf.html')

def actwiki_lineages_gnome(request):
    return render(request, 'session/actcompendium/lineages/gnome.html')

def actwiki_lineages_halfelf(request):
    return render(request, 'session/actcompendium/lineages/halfelf.html')

def actwiki_lineages_halforc(request):
    return render(request, 'session/actcompendium/lineages/halforc.html')

def actwiki_lineages_halfling(request):
    return render(request, 'session/actcompendium/lineages/halfling.html')

def actwiki_lineages_human(request):
    return render(request, 'session/actcompendium/lineages/human.html')

def actwiki_lineages_tiefling(request):
    return render(request, 'session/actcompendium/lineages/tiefling.html')

def character_menu(request):
    return render(request, 'session/characterCreation/character_menu.html')

def create_character(request):
    if request.method == 'POST':
        # Extract data from the form
        name = request.POST.get('name')
        race = request.POST.get('race')
        char_class = request.POST.get('char_class')
        background = request.POST.get('background')
        try:
            strength = int(request.POST.get('strength'))
            dexterity = int(request.POST.get('dexterity'))
            constitution = int(request.POST.get('constitution'))
            intelligence = int(request.POST.get('intelligence'))
            wisdom = int(request.POST.get('wisdom'))
            charisma = int(request.POST.get('charisma'))
        except ValueError:
            # Handle the case where conversion fails
            messages.error(request, "All stats must be valid integers.")
            return render(request, 'session/characterCreation/create/create_character.html')

        # Collect all the stats in a list
        stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

        # Check if any stats have the same value
        if len(stats) != len(set(stats)):
            # If there are duplicates, show an error message
            messages.error(request, "No two stats should have the same value!")
            return render(request, 'session/characterCreation/create/create_character.html', {
                'name': name,
                'race': race,
                'char_class': char_class,
                'background': background,
                'strength': strength,
                'dexterity': dexterity,
                'constitution': constitution,
                'intelligence': intelligence,
                'wisdom': wisdom,
                'charisma': charisma,
            })

        # Define race-based stat bonuses
        race_stat_modifiers = {
            "dragonborn": {"strength": 2, "charisma": 1},
            "dwarf": {"constitution": 2},
            "elf": {"dexterity": 2},
            "gnome": {"intelligence": 2, "dexterity": 1},
            "half-elf": {"charisma": 2, "intelligence": 1, "wisdom": 1},
            "half-orc": {"strength": 2, "constitution": 1},
            "halfling": {"dexterity": 2, "charisma": 1},
            "human": {"strength": 1, "dexterity": 1, "constitution": 1, "intelligence": 1, "wisdom": 1, "charisma": 1},
            "tiefling": {"charisma": 2, "intelligence": 1},
        }

        # Apply race-based stat bonuses if race exists in the dictionary
        if race.lower() in race_stat_modifiers:
            modifiers = race_stat_modifiers[race.lower()]
            strength += modifiers.get("strength", 0)
            dexterity += modifiers.get("dexterity", 0)
            constitution += modifiers.get("constitution", 0)
            intelligence += modifiers.get("intelligence", 0)
            wisdom += modifiers.get("wisdom", 0)
            charisma += modifiers.get("charisma", 0)

                # Create the character instance and save to the database
        character = Character(
            user=request.user,
            name=name,
            race=race,
            char_class=char_class,
            background=background,
            strength=strength,
            dexterity=dexterity,
            constitution=constitution,
            intelligence=intelligence,
            wisdom=wisdom,
            charisma=charisma
        )
        character.save()

        # Redirect to a page, such as the character customization page
        return redirect('customize_character', character_id=character.id)

    return render(request, 'session/characterCreation/create/create_character.html')

def customize_character(request, character_id):
    # Fetch the character object, ensuring it belongs to the logged-in user
    character = get_object_or_404(Character, id=character_id, user=request.user)

    # Get all available spells, weapons, and equipment
    spells = Spell.objects.all()
    weapons = Weapon.objects.all()
    equipments = Equipment.objects.all()

    if request.method == 'POST':
        # Get selected spells, weapons, and equipment from the form
        selected_spells = request.POST.getlist('spells')
        primary_weapon = request.POST.get('primary_weapon')
        secondary_weapon = request.POST.get('secondary_weapon')
        selected_equipments = request.POST.getlist('equipments')


        # Combine primary and secondary weapons into a list
        selected_weapons = [primary_weapon, secondary_weapon]

        # Validation for spells
        spell_counts = {
            'level_4': 0,
            'level_3': 0,
            'level_2': 0,
            'level_1': 0,
        }

        # Count spells by level
        for spell_id in selected_spells:
            spell = Spell.objects.get(id=spell_id)
            if spell.level == 4:
                spell_counts['level_4'] += 1
            elif spell.level == 3:
                spell_counts['level_3'] += 1
            elif spell.level == 2:
                spell_counts['level_2'] += 1
            elif spell.level == 1:
                spell_counts['level_1'] += 1

        # Validate spell selection
        if (spell_counts['level_4'] != 1 or
            spell_counts['level_3'] != 1 or
            spell_counts['level_2'] != 2 or
            spell_counts['level_1'] != 2):
            messages.error(request, "You must select exactly 1 Level 4 spell, 1 Level 3 spell, 2 Level 2 spells, and 2 Level 1 spells.")
            return redirect('customize_character', character_id=character.id)

        # Validation for weapons (1 primary and 1 secondary)
        if len(selected_weapons) != 2:
            messages.error(request, "You must select exactly 2 weapons: 1 Primary and 1 Secondary.")
            return redirect('customize_character', character_id=character.id)

        # Validation for equipment (at least 7 items)
        if len(selected_equipments) < 7:
            messages.error(request, "You must select at least 7 pieces of equipment.")
            return redirect('customize_character', character_id=character.id)

        # Create or update the Customization for this character
        customization, created = Customization.objects.get_or_create(character=character)
        customization.spells.set(selected_spells)
        customization.weapons.set(selected_weapons)
        customization.equipments.set(selected_equipments)
        customization.save()

        # Redirect to a page to view the character or confirmation page
        return redirect('character_review', character_id=character.id)

    return render(request, 'session/characterCreation/create/customize_character.html', {
        'character': character,
        'spells': spells,
        'weapons': weapons,
        'equipments': equipments,
    })

def delete_character(request, character_id):
    # Ensure the character belongs to the logged-in user
    character = get_object_or_404(Character, id=character_id, user=request.user)
    character.delete()  # Delete the character from the database
    return redirect('character_menu')  # Redirect to the character menu

def character_review(request, character_id):
    # Get the character and customization data
    character = get_object_or_404(Character, id=character_id)
    customization = get_object_or_404(Customization, character=character)

    return render(request, 'session/characterCreation/create/character_review.html', {
        'character': character,
        'customization': customization
    })

def update_character_details(request, character_id):
    # Fetch the character from the database using the provided character_id
    character = get_object_or_404(Character, id=character_id)

    # Define race-based stat bonuses
    race_stat_modifiers = {
        "dragonborn": {"strength": 2, "charisma": 1},
        "dwarf": {"constitution": 2},
        "elf": {"dexterity": 2},
        "gnome": {"intelligence": 2, "dexterity": 1},
        "half-elf": {"charisma": 2, "intelligence": 1, "wisdom": 1},
        "half-orc": {"strength": 2, "constitution": 1},
        "halfling": {"dexterity": 2, "charisma": 1},
        "human": {"strength": 1, "dexterity": 1, "constitution": 1, "intelligence": 1, "wisdom": 1, "charisma": 1},
        "tiefling": {"charisma": 2, "intelligence": 1},
    }

    # Get the race modifier for the character's current race
    race = character.race.lower()
    modifiers = race_stat_modifiers.get(race, {})

    # Subtract the race-based modifiers from the stats to get the original values
    original_strength = character.strength - modifiers.get("strength", 0)
    original_dexterity = character.dexterity - modifiers.get("dexterity", 0)
    original_constitution = character.constitution - modifiers.get("constitution", 0)
    original_intelligence = character.intelligence - modifiers.get("intelligence", 0)
    original_wisdom = character.wisdom - modifiers.get("wisdom", 0)
    original_charisma = character.charisma - modifiers.get("charisma", 0)

    if request.method == 'POST':
        # Attempt to get the updated stat values from the form
        try:
            strength = int(request.POST.get('strength', original_strength))
            dexterity = int(request.POST.get('dexterity', original_dexterity))
            constitution = int(request.POST.get('constitution', original_constitution))
            intelligence = int(request.POST.get('intelligence', original_intelligence))
            wisdom = int(request.POST.get('wisdom', original_wisdom))
            charisma = int(request.POST.get('charisma', original_charisma))  # Get Charisma from POST
        except ValueError:
            messages.error(request, "All stats must be valid integers.")
            return render(request, 'session/characterCreation/create/update_character_details.html', {'character': character})

        # Debugging print statements
        print(f"Original Charisma: {original_charisma}")
        print(f"Charisma from POST: {request.POST.get('charisma')}")
        print(f"Final Charisma after applying modifiers: {charisma}")

        # Collect all the stats in a list
        stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

        # Check if any stats have the same value
        if len(stats) != len(set(stats)):
            # If there are duplicates, show an error message
            messages.error(request, "No two stats should have the same value!")
            return render(request, 'session/characterCreation/create/update_character_details.html', {
                'character': character,
                'strength': strength,
                'dexterity': dexterity,
                'constitution': constitution,
                'intelligence': intelligence,
                'wisdom': wisdom,
                'charisma': charisma,
            })

        # Apply race-based stat bonuses after the user submits the form
        if character.race.lower() in race_stat_modifiers:
            modifiers = race_stat_modifiers[character.race.lower()]
            strength += modifiers.get("strength", 0)
            dexterity += modifiers.get("dexterity", 0)
            constitution += modifiers.get("constitution", 0)
            intelligence += modifiers.get("intelligence", 0)
            wisdom += modifiers.get("wisdom", 0)
            charisma += modifiers.get("charisma", 0)  # Apply race-based bonus

        # Assign the updated stats back to the character object
        character.strength = strength
        character.dexterity = dexterity
        character.constitution = constitution
        character.intelligence = intelligence
        character.wisdom = wisdom
        character.charisma = charisma

        # Save the updated character object to the database
        character.save()

        # After saving, redirect back to the character review page
        return redirect('character_review', character_id=character.id)

    # If the request method is GET, pass the character to the template to pre-populate the form
    return render(request, 'session/characterCreation/create/update_character_details.html', {
        'character': character,
        'original_strength': original_strength,
        'original_dexterity': original_dexterity,
        'original_constitution': original_constitution,
        'original_intelligence': original_intelligence,
        'original_wisdom': original_wisdom,
        'original_charisma': original_charisma,
    })

def update_character_customization(request, character_id):
    # Fetch the character object, ensuring it belongs to the logged-in user
    character = get_object_or_404(Character, id=character_id, user=request.user)

    # Get all available spells, weapons, and equipment
    spells = Spell.objects.all()
    weapons = Weapon.objects.all()
    equipments = Equipment.objects.all()

    # Fetch existing customization if it exists
    customization = Customization.objects.filter(character=character).first()

    # If the request method is POST, process the form
    if request.method == 'POST':
        # Get selected spells, weapons, and equipment from the form
        selected_spells = request.POST.getlist('spells')
        primary_weapon = request.POST.get('primary_weapon')
        secondary_weapon = request.POST.get('secondary_weapon')
        selected_equipments = request.POST.getlist('equipments')

        # Combine primary and secondary weapons into a list
        selected_weapons = [primary_weapon, secondary_weapon]

        # Validation for spells
        spell_counts = {
            'level_4': 0,
            'level_3': 0,
            'level_2': 0,
            'level_1': 0,
        }

        # Count spells by level
        for spell_id in selected_spells:
            spell = Spell.objects.get(id=spell_id)
            if spell.level == 4:
                spell_counts['level_4'] += 1
            elif spell.level == 3:
                spell_counts['level_3'] += 1
            elif spell.level == 2:
                spell_counts['level_2'] += 1
            elif spell.level == 1:
                spell_counts['level_1'] += 1

        # Validate spell selection
        if (spell_counts['level_4'] != 1 or
            spell_counts['level_3'] != 1 or
            spell_counts['level_2'] != 2 or
            spell_counts['level_1'] != 2):
            messages.error(request, "You must select exactly 1 Level 4 spell, 1 Level 3 spell, 2 Level 2 spells, and 2 Level 1 spells.")
            return redirect('update_character_customization', character_id=character.id)

        # Validation for weapons (1 primary and 1 secondary)
        if len(selected_weapons) != 2:
            messages.error(request, "You must select exactly 2 weapons: 1 Primary and 1 Secondary.")
            return redirect('update_character_customization', character_id=character.id)

        # Validation for equipment (at least 7 items)
        if len(selected_equipments) < 7:
            messages.error(request, "You must select at least 7 pieces of equipment.")
            return redirect('update_character_customization', character_id=character.id)

        # Update or create the Customization for this character
        if customization:
            # Update existing customization
            customization.spells.set(selected_spells)
            customization.weapons.set(selected_weapons)
            customization.equipments.set(selected_equipments)
            customization.save()
        else:
            # Create new customization if none exists
            customization = Customization.objects.create(character=character)
            customization.spells.set(selected_spells)
            customization.weapons.set(selected_weapons)
            customization.equipments.set(selected_equipments)
            customization.save()

        # Redirect to a page to view the character or confirmation page
        return redirect('character_review', character_id=character.id)

    return render(request, 'session/characterCreation/create/update_character_customization.html', {
        'character': character,
        'spells': spells,
        'weapons': weapons,
        'equipments': equipments,
        'customization': customization,  # Pass existing customization data if it exists
    })

def render_to_pdf(template_src, context_dict={}):
    """
    Renders an HTML template into a PDF using WeasyPrint.
    """
    template = get_template(template_src)
    html = template.render(context_dict)
    
    # Use WeasyPrint to convert HTML to PDF
    pdf = weasyprint.HTML(string=html).write_pdf()
    
    # Create the HTTP response with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="character_sheet.pdf"'
    return response

def generate_character_pdf(request, character_id):
    # Fetch character and customization data
    try:
        character = Character.objects.get(id=character_id, user=request.user)
        customization = Customization.objects.get(character=character)
    except (Character.DoesNotExist, Customization.DoesNotExist):
        return HttpResponse("Character not found or you don't have access.", status=404)

    # Prepare the context for the template
    context = {
        'character': character,
        'customization': customization,
    }

    # Debug: Check the types of key fields (e.g., stats, spells)
    print(f"Strength: {character.strength}, Type: {type(character.strength)}")
    print(f"Dexterity: {character.dexterity}, Type: {type(character.dexterity)}")

    # Render the PDF using an HTML template
    return render_to_pdf('session/characterCreation/create/character_sheet_layout.html', context)
