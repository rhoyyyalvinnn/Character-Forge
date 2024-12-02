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

# ALL BACKGROUNDS
def actwiki_backgrounds_acolyte(request):
    return render(request, 'session/actcompendium/backgrounds/acolyte.html')

def actwiki_backgrounds_athlete(request):
    return render(request, 'session/actcompendium/backgrounds/athlete.html')

def actwiki_backgrounds_anthropologist(request):
    return render(request, 'session/actcompendium/backgrounds/anthropologist.html')

def actwiki_backgrounds_archaeologist(request):
    return render(request, 'session/actcompendium/backgrounds/archaeologist.html')

def actwiki_backgrounds_athelete(request):
    return render(request, 'session/actcompendium/backgrounds/athelete.html')

def actwiki_backgrounds_charlatan(request):
    return render(request, 'session/actcompendium/backgrounds/charlatan.html')

def actwiki_backgrounds_citywatch(request):
    return render(request, 'session/actcompendium/backgrounds/citywatch.html')

def actwiki_backgrounds_clancrafter(request):
    return render(request, 'session/actcompendium/backgrounds/clancrafter.html')

def actwiki_backgrounds_cloisteredscholar(request):
    return render(request, 'session/actcompendium/backgrounds/cloisteredscholar.html')

def actwiki_backgrounds_courtier(request):
    return render(request, 'session/actcompendium/backgrounds/courtier.html')

def actwiki_backgrounds_criminal(request):
    return render(request, 'session/actcompendium/backgrounds/criminal.html')

def actwiki_backgrounds_entertainer(request):
    return render(request, 'session/actcompendium/backgrounds/entertainer.html')

def actwiki_backgrounds_faceless(request):
    return render(request, 'session/actcompendium/backgrounds/faceless.html')

def actwiki_backgrounds_factionagent(request):
    return render(request, 'session/actcompendium/backgrounds/factionagent.html')

def actwiki_backgrounds_fartraveler(request):
    return render(request, 'session/actcompendium/backgrounds/fartraveler.html')

def actwiki_backgrounds_feylost(request):
    return render(request, 'session/actcompendium/backgrounds/feylost.html')

def actwiki_backgrounds_fisher(request):
    return render(request, 'session/actcompendium/backgrounds/fisher.html')

def actwiki_backgrounds_folkhero(request):
    return render(request, 'session/actcompendium/backgrounds/folkhero.html')

def actwiki_backgrounds_giantfoundling(request):
    return render(request, 'session/actcompendium/backgrounds/giantfoundling.html')

def actwiki_backgrounds_gladiator(request):
    return render(request, 'session/actcompendium/backgrounds/gladiator.html')

def actwiki_backgrounds_guildartisan(request):
    return render(request, 'session/actcompendium/backgrounds/guildartisan.html')

def actwiki_backgrounds_guildmerchant(request):
    return render(request, 'session/actcompendium/backgrounds/guildmerchant.html')

def actwiki_backgrounds_hauntedone(request):
    return render(request, 'session/actcompendium/backgrounds/hauntedone.html')

def actwiki_backgrounds_hermit(request):
    return render(request, 'session/actcompendium/backgrounds/hermit.html')

def actwiki_backgrounds_houseagent(request):
    return render(request, 'session/actcompendium/backgrounds/houseagent.html')

def actwiki_backgrounds_inheritor(request):
    return render(request, 'session/actcompendium/backgrounds/inheritor.html')

def actwiki_backgrounds_investigator_scag(request):
    return render(request, 'session/actcompendium/backgrounds/investigator_scag.html')

def actwiki_backgrounds_investigator_vrgr(request):
    return render(request, 'session/actcompendium/backgrounds/investigator_vrgr.html')

def actwiki_backgrounds_knight(request):
    return render(request, 'session/actcompendium/backgrounds/knight.html')

def actwiki_backgrounds_knightoftheorder(request):
    return render(request, 'session/actcompendium/backgrounds/knightoftheorder.html')

def actwiki_backgrounds_marine(request):
    return render(request, 'session/actcompendium/backgrounds/marine.html')

def actwiki_backgrounds_mercenaryveteran(request):
    return render(request, 'session/actcompendium/backgrounds/mercenaryveteran.html')

def actwiki_backgrounds_noble(request):
    return render(request, 'session/actcompendium/backgrounds/noble.html')

def actwiki_backgrounds_outlander(request):
    return render(request, 'session/actcompendium/backgrounds/outlander.html')

def actwiki_backgrounds_pirate(request):
    return render(request, 'session/actcompendium/backgrounds/pirate.html')

def actwiki_backgrounds_rewarded(request):
    return render(request, 'session/actcompendium/backgrounds/rewarded.html')

def actwiki_backgrounds_ruined(request):
    return render(request, 'session/actcompendium/backgrounds/ruined.html')

def actwiki_backgrounds_runecarver(request):
    return render(request, 'session/actcompendium/backgrounds/runecarver.html')

def actwiki_backgrounds_sage(request):
    return render(request, 'session/actcompendium/backgrounds/sage.html')

def actwiki_backgrounds_sailor(request):
    return render(request, 'session/actcompendium/backgrounds/sailor.html')

def actwiki_backgrounds_shipwright(request):
    return render(request, 'session/actcompendium/backgrounds/shipwright.html')

def actwiki_backgrounds_smuggler(request):
    return render(request, 'session/actcompendium/backgrounds/smuggler.html')

def actwiki_backgrounds_soldier(request):
    return render(request, 'session/actcompendium/backgrounds/soldier.html')

def actwiki_backgrounds_spy(request):
    return render(request, 'session/actcompendium/backgrounds/spy.html')

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
            # Extract base stats from the form
            base_strength = int(request.POST.get('strength'))
            base_dexterity = int(request.POST.get('dexterity'))
            base_constitution = int(request.POST.get('constitution'))
            base_intelligence = int(request.POST.get('intelligence'))
            base_wisdom = int(request.POST.get('wisdom'))
            base_charisma = int(request.POST.get('charisma'))
        except ValueError:
            # Handle the case where conversion fails
            messages.error(request, "All stats must be valid integers.")
            return render(request, 'session/characterCreation/create/create_character.html')

        # Collect all the stats in a list
        base_stats = [base_strength, base_dexterity, base_constitution, base_intelligence, base_wisdom, base_charisma]

        # Check if any stats have the same value
        if len(base_stats) != len(set(base_stats)):
            # If there are duplicates, show an error message
            messages.error(request, "No two stats should have the same value!")
            return render(request, 'session/characterCreation/create/create_character.html', {
                'name': name,
                'race': race,
                'char_class': char_class,
                'background': background,
                'strength': base_strength,
                'dexterity': base_dexterity,
                'constitution': base_constitution,
                'intelligence': base_intelligence,
                'wisdom': base_wisdom,
                'charisma': base_charisma,
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

        # Calculate final stats by applying race-based stat bonuses
        final_strength = base_strength
        final_dexterity = base_dexterity
        final_constitution = base_constitution
        final_intelligence = base_intelligence
        final_wisdom = base_wisdom
        final_charisma = base_charisma

        # Apply race-based stat bonuses if race exists in the dictionary
        if race.lower() in race_stat_modifiers:
            modifiers = race_stat_modifiers[race.lower()]
            final_strength += modifiers.get("strength", 0)
            final_dexterity += modifiers.get("dexterity", 0)
            final_constitution += modifiers.get("constitution", 0)
            final_intelligence += modifiers.get("intelligence", 0)
            final_wisdom += modifiers.get("wisdom", 0)
            final_charisma += modifiers.get("charisma", 0)

        # Create the character instance and save to the database
        character = Character(
            user=request.user,
            name=name,
            race=race,
            char_class=char_class,
            background=background,
            # Save base stats
            base_strength=base_strength,
            base_dexterity=base_dexterity,
            base_constitution=base_constitution,
            base_intelligence=base_intelligence,
            base_wisdom=base_wisdom,
            base_charisma=base_charisma,
            # Save final stats
            final_strength=final_strength,
            final_dexterity=final_dexterity,
            final_constitution=final_constitution,
            final_intelligence=final_intelligence,
            final_wisdom=final_wisdom,
            final_charisma=final_charisma
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

        print(selected_spells)
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
        if primary_weapon == secondary_weapon:
            messages.error(request, "The primary and secondary weapons cannot be the same.")
            return redirect('customize_character', character_id=character.id)

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
    print(f"Starting update_character_details for character ID: {character_id}")

    # Fetch the character from the database using the provided character_id
    character = get_object_or_404(Character, id=character_id)
    print(f"Fetched character: {character.name} (ID: {character.id})")

    # Use base stats as original stats
    original_strength = character.base_strength
    original_dexterity = character.base_dexterity
    original_constitution = character.base_constitution
    original_intelligence = character.base_intelligence
    original_wisdom = character.base_wisdom
    original_charisma = character.base_charisma
    print(f"Original stats: STR={original_strength}, DEX={original_dexterity}, CON={original_constitution}, "
          f"INT={original_intelligence}, WIS={original_wisdom}, CHA={original_charisma}")

    if request.method == 'POST':
        print("Processing POST request...")

        # Attempt to get the updated values from the form
        name = request.POST.get('name')
        new_race = request.POST.get('race')
        char_class = request.POST.get('char_class')
        background = request.POST.get('background')
        print(f"Form data: name={name}, race={new_race}, class={char_class}, background={background}")

        try:
            new_base_strength = int(request.POST.get('strength'))
            new_base_dexterity = int(request.POST.get('dexterity'))
            new_base_constitution = int(request.POST.get('constitution'))
            new_base_intelligence = int(request.POST.get('intelligence'))
            new_base_wisdom = int(request.POST.get('wisdom'))
            new_base_charisma = int(request.POST.get('charisma'))
            print(f"New base stats: STR={new_base_strength}, DEX={new_base_dexterity}, CON={new_base_constitution}, "
                  f"INT={new_base_intelligence}, WIS={new_base_wisdom}, CHA={new_base_charisma}")
        except ValueError:
            print("Error: One or more stats are not valid integers.")
            messages.error(request, "All stats must be valid integers.")
            return render(request, 'session/characterCreation/create/update_character_details.html', {'character': character})

        # Collect all the stats in a list
        new_base_stats = [
            new_base_strength,
            new_base_dexterity,
            new_base_constitution,
            new_base_intelligence,
            new_base_wisdom,
            new_base_charisma,
        ]

        # Check if any stats have the same value
        if len(new_base_stats) != len(set(new_base_stats)):
            print("Validation failed: Duplicate stats detected.")
            messages.error(request, "No two stats should have the same value!")
            return render(request, 'session/characterCreation/create/update_character_details.html', {
                'character': character,
                'strength': new_base_strength,
                'dexterity': new_base_dexterity,
                'constitution': new_base_constitution,
                'intelligence': new_base_intelligence,
                'wisdom': new_base_wisdom,
                'charisma': new_base_charisma,
            })

        # Define race-based stat modifiers
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

        # Apply race-based modifiers to calculate final stats
        modifiers = race_stat_modifiers.get(new_race.lower(), {})
        print(f"Race modifiers for {new_race}: {modifiers}")

        new_strength = new_base_strength + modifiers.get("strength", 0)
        new_dexterity = new_base_dexterity + modifiers.get("dexterity", 0)
        new_constitution = new_base_constitution + modifiers.get("constitution", 0)
        new_intelligence = new_base_intelligence + modifiers.get("intelligence", 0)
        new_wisdom = new_base_wisdom + modifiers.get("wisdom", 0)
        new_charisma = new_base_charisma + modifiers.get("charisma", 0)

        print(f"Final stats after modifiers: STR={new_strength}, DEX={new_dexterity}, CON={new_constitution}, "
              f"INT={new_intelligence}, WIS={new_wisdom}, CHA={new_charisma}")

        # Update character attributes
        character.name = name
        character.race = new_race
        character.char_class = char_class
        character.background = background

        # Update both base and final stats
        character.base_strength = new_base_strength
        character.base_dexterity = new_base_dexterity
        character.base_constitution = new_base_constitution
        character.base_intelligence = new_base_intelligence
        character.base_wisdom = new_base_wisdom
        character.base_charisma = new_base_charisma

        character.final_strength = new_strength
        character.final_dexterity = new_dexterity
        character.final_constitution = new_constitution
        character.final_intelligence = new_intelligence
        character.final_wisdom = new_wisdom
        character.final_charisma = new_charisma

        # Save the updated character object to the database
        character.save()
        print(f"Character {character.name} (ID: {character.id}) updated successfully.")

        # Redirect to the character review page
        return redirect('character_review', character_id=character.id)

    print("Rendering character update form.")
    # If the request method is GET, pass the character and base stats to the template
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

                # Validation for weapons (1 primary and 1 secondary)
        if primary_weapon == secondary_weapon:
            messages.error(request, "The primary and secondary weapons cannot be the same.")
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
    # This will open the PDF in a new tab (browsers typically use new tabs for inline PDF viewing)
    response['Content-Disposition'] = 'inline; filename="character_sheet.pdf"'
    
    # Add a header to suggest opening the file in a new tab
    response['X-Content-Type-Options'] = 'nosniff'
    
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

    # Debug: Check the types of key fields


    # Render the PDF using an HTML template
    return render_to_pdf('session/characterCreation/create/character_sheet_layout.html', context)



