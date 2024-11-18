from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
def home(request):
    # Access the logged-in user's details directly
    user = request.user  # This is the authenticated user object

    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, "session/homepage.html", context)

def signout(request):
    logout(request)  # Logs the user out
    return redirect('index')  # Redirect to index or homepage after logging out


def profile(request):
        # Access the logged-in user's details directly
    user = request.user  # This is the authenticated user object

    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        # Add more fields if needed
    }
    return render(request, "session/profile.html", context)



def actgamerules(request):
    return render(request, "session/actgamerules.html")

def actcommunity(request):
    return render(request, "session/actcommunity.html")

def actforum(request):
    return render(request, "session/actforum.html")



# chatgpt code for creating pdf using html
# https://chatgpt.com/c/67356442-f244-800f-b2aa-3ac658a6e4fb

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

