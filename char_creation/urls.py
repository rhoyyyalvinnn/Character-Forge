from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('actcommunity/', views.actcommunity, name='actcommunity'),
    path('actforum/', views.actforum, name='actforum'),
    path('actgamerules/', views.actgamerules, name='actgamerules'),
    path('actcompendium/', views.actcompendium, name="actcompendium"),
    path('actcompendium/artificer/', views.actwiki_spells_artificer, name="actwiki_spells_artificer"),
    path('actcompendium/bard/', views.actwiki_spells_bard, name="actwiki_spells_bard"),
    path('actcompendium/cleric/', views.actwiki_spells_cleric, name="actwiki_spells_cleric"),
    path('actcompendium/druid/', views.actwiki_spells_druid, name="actwiki_spells_druid"),
    path('actcompendium/paladin/', views.actwiki_spells_paladin, name="actwiki_spells_paladin"),
    path('actcompendium/ranger/', views.actwiki_spells_ranger, name="actwiki_spells_ranger"),
    path('actcompendium/sorcerer/', views.actwiki_spells_sorcerer, name="actwiki_spells_sorcerer"),
    path('actcompendium/warlock/', views.actwiki_spells_warlock, name="actwiki_spells_warlock"),
    path('actcompendium/wizard/', views.actwiki_spells_wizard, name="actwiki_spells_wizard"),
    path('menu/', views.character_menu, name="character_menu"),
    path('character_creation',views.character_creation, name='character_creation'),
    path('race/', views.character_race, name="character_race"),
    path('class/', views.character_class, name="character_class"),
    path('abilities/', views.character_abilities, name="character_abilities"),
    path('backgrounds/', views.character_background, name="character_background"),
    path('equipments/', views.character_equipment, name="character_equipment"),
    path('spells/', views.character_spell, name="character_spell"),
    path('feats/', views.character_feats, name="character_feats"),
    path('bio/', views.character_bio, name="character_bio"),
    # path('save_race/', views.save_race, name='save_race'),
]