from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in first
            return redirect('home')  # Construct the URL correctly
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('signin')

    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        conf_pass = request.POST.get('password2')

        # Check if passwords match
        if password != conf_pass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')  # Redirect back to the signup page


        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('signup')

        # Check if email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('signup')



        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('signin')

    return render(request, "authentication/signup.html")



def signin(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in first
            return redirect('home')  # Construct the URL correctly
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('index')

    return render(request, "authentication/signin.html")

def signout(request):
    pass


def gamerules(request):
    return render(request, "gamerules.html")

def community(request):
    return render(request, "community.html")

def forum(request):
    return render(request, "forum.html")

def compendium(request):
    return render(request, 'compendium/compendium.html')

def wiki_spells_artificer(request):
    return render(request, 'compendium/spells/artificer_spell.html')

def wiki_spells_bard(request):
    return render(request, 'compendium/spells/bard_spell.html')

def wiki_spells_cleric(request):
    return render(request, 'compendium/spells/cleric_spell.html')

def wiki_spells_druid(request):
    return render(request, 'compendium/spells/druid_spell.html')

def wiki_spells_paladin(request):
    return render(request, 'compendium/spells/paladin_spell.html')

def wiki_spells_ranger(request):
    return render(request, 'compendium/spells/ranger_spell.html')

def wiki_spells_sorcerer(request):
    return render(request, 'compendium/spells/sorcerer_spell.html')

def wiki_spells_warlock(request):
    return render(request, 'compendium/spells/warlock_spell.html')

def wiki_spells_wizard(request):
    return render(request, 'compendium/spells/wizard_spell.html')

def wiki_lineages_dragonborn(request):
    return render(request, 'compendium/lineages/dragonborn.html')

def wiki_lineages_dwarf(request):
    return render(request, 'compendium/lineages/dwarf.html')

def wiki_lineages_elf(request):
    return render(request, 'compendium/lineages/elf.html')

def wiki_lineages_gnome(request):
    return render(request, 'compendium/lineages/gnome.html')

def wiki_lineages_halfelf(request):
    return render(request, 'compendium/lineages/halfelf.html')

def wiki_lineages_halforc(request):
    return render(request, 'compendium/lineages/halforc.html')

def wiki_lineages_halfling(request):
    return render(request, 'compendium/lineages/halfling.html')

def wiki_lineages_human(request):
    return render(request, 'compendium/lineages/human.html')

def wiki_lineages_tiefling(request):
    return render(request, 'compendium/lineages/tiefling.html')




#  ALL BACKGROUNDS

def wiki_backgrounds_acolyte(request):
    return render(request, 'compendium/backgrounds/acolyte.html')

def wiki_backgrounds_athlete(request):
    return render(request, 'compendium/backgrounds/athlete.html')

def wiki_backgrounds_anthropologist(request):
    return render(request, 'compendium/backgrounds/anthropologist.html')

def wiki_backgrounds_archaeologist(request):
    return render(request, 'compendium/backgrounds/archaeologist.html')

def wiki_backgrounds_athelete(request):
    return render(request, 'compendium/backgrounds/athelete.html')

def wiki_backgrounds_charlatan(request):
    return render(request, 'compendium/backgrounds/charlatan.html')

def wiki_backgrounds_citywatch(request):
    return render(request, 'compendium/backgrounds/citywatch.html')

def wiki_backgrounds_clancrafter(request):
    return render(request, 'compendium/backgrounds/clancrafter.html')

def wiki_backgrounds_cloisteredscholar(request):
    return render(request, 'compendium/backgrounds/cloisteredscholar.html')

def wiki_backgrounds_courtier(request):
    return render(request, 'compendium/backgrounds/courtier.html')

def wiki_backgrounds_criminal(request):
    return render(request, 'compendium/backgrounds/criminal.html')

def wiki_backgrounds_entertainer(request):
    return render(request, 'compendium/backgrounds/entertainer.html')

def wiki_backgrounds_faceless(request):
    return render(request, 'compendium/backgrounds/faceless.html')

def wiki_backgrounds_factionagent(request):
    return render(request, 'compendium/backgrounds/factionagent.html')

def wiki_backgrounds_fartraveler(request):
    return render(request, 'compendium/backgrounds/fartraveler.html')

def wiki_backgrounds_feylost(request):
    return render(request, 'compendium/backgrounds/feylost.html')

def wiki_backgrounds_fisher(request):
    return render(request, 'compendium/backgrounds/fisher.html')

def wiki_backgrounds_folkhero(request):
    return render(request, 'compendium/backgrounds/folkhero.html')

def wiki_backgrounds_giantfoundling(request):
    return render(request, 'compendium/backgrounds/giantfoundling.html')

def wiki_backgrounds_gladiator(request):
    return render(request, 'compendium/backgrounds/gladiator.html')

def wiki_backgrounds_guildartisan(request):
    return render(request, 'compendium/backgrounds/guildartisan.html')

def wiki_backgrounds_guildmerchant(request):
    return render(request, 'compendium/backgrounds/guildmerchant.html')

def wiki_backgrounds_hauntedone(request):
    return render(request, 'compendium/backgrounds/hauntedone.html')

def wiki_backgrounds_hermit(request):
    return render(request, 'compendium/backgrounds/hermit.html')

def wiki_backgrounds_houseagent(request):
    return render(request, 'compendium/backgrounds/houseagent.html')

def wiki_backgrounds_inheritor(request):
    return render(request, 'compendium/backgrounds/inheritor.html')

def wiki_backgrounds_investigator_scag(request):
    return render(request, 'compendium/backgrounds/investigator_scag.html')

def wiki_backgrounds_investigator_vrgr(request):
    return render(request, 'compendium/backgrounds/investigator_vrgr.html')

def wiki_backgrounds_knight(request):
    return render(request, 'compendium/backgrounds/knight.html')

def wiki_backgrounds_knightoftheorder(request):
    return render(request, 'compendium/backgrounds/knightoftheorder.html')

def wiki_backgrounds_marine(request):
    return render(request, 'compendium/backgrounds/marine.html')

def wiki_backgrounds_mercenaryveteran(request):
    return render(request, 'compendium/backgrounds/mercenaryveteran.html')

def wiki_backgrounds_noble(request):
    return render(request, 'compendium/backgrounds/noble.html')

def wiki_backgrounds_outlander(request):
    return render(request, 'compendium/backgrounds/outlander.html')

def wiki_backgrounds_pirate(request):
    return render(request, 'compendium/backgrounds/pirate.html')

def wiki_backgrounds_rewarded(request):
    return render(request, 'compendium/backgrounds/rewarded.html')

def wiki_backgrounds_ruined(request):
    return render(request, 'compendium/backgrounds/ruined.html')

def wiki_backgrounds_runecarver(request):
    return render(request, 'compendium/backgrounds/runecarver.html')

def wiki_backgrounds_sage(request):
    return render(request, 'compendium/backgrounds/sage.html')

def wiki_backgrounds_sailor(request):
    return render(request, 'compendium/backgrounds/sailor.html')

def wiki_backgrounds_shipwright(request):
    return render(request, 'compendium/backgrounds/shipwright.html')

def wiki_backgrounds_smuggler(request):
    return render(request, 'compendium/backgrounds/smuggler.html')

def wiki_backgrounds_soldier(request):
    return render(request, 'compendium/backgrounds/soldier.html')

def wiki_backgrounds_spy(request):
    return render(request, 'compendium/backgrounds/spy.html')


