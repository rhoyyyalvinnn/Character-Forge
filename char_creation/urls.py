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
    path('actcompendium/dragonborn', views.actwiki_lineages_dragonborn, name="actwiki_lineages_dragonborn"),
    path('actcompendium/elf', views.actwiki_lineages_elf, name="actwiki_lineages_elf"),
    path('actcompendium/gnome', views.actwiki_lineages_gnome, name="actwiki_lineages_gnome"),
    path('actcompendium/halfelf', views.actwiki_lineages_halfelf, name="actwiki_lineages_halfelf"),
    path('actcompendium/halforc', views.actwiki_lineages_halforc, name="actwiki_lineages_halforc"),
    path('actcompendium/halfling', views.actwiki_lineages_halfling, name="actwiki_lineages_halfling"),
    path('actcompendium/human', views.actwiki_lineages_human, name="actwiki_lineages_human"),
    path('actcompendium/tiefling', views.actwiki_lineages_tiefling, name="actwiki_lineages_tiefling"),
    path('actcompendium/dwarf', views.actwiki_lineages_dwarf, name="actwiki_lineages_dwarf"),
    # other compedium stuffs

    path('menu/', views.character_menu, name="character_menu"),
    path('create/', views.create_character, name='create_character'),
    path('character/customize/<int:character_id>/', views.customize_character, name='customize_character')
    # path('customize/<int:character_id>/', views.customize_character, name='customize_character'),















    # path('character_creation',views.character_creation, name='character_creation'),
    # path('race/', views.character_race, name="character_race"),
    # path('class/', views.character_class, name="character_class"),
    # path('abilities/', views.character_abilities, name="character_abilities"),
    # path('backgrounds/', views.character_background, name="character_background"),
    # path('equipments/', views.character_equipment, name="character_equipment"),
    # path('spells/', views.character_spell, name="character_spell"),
    # path('feats/', views.character_feats, name="character_feats"),
    # path('bio/', views.character_bio, name="character_bio"),
    # path('save_race/', views.save_race, name='save_race'),
    # path for charactercreationthings
    # path('save_character/', views.save_character, name='save_character'),
]







