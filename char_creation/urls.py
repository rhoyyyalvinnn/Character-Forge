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
    path('character/customize/<int:character_id>/', views.customize_character, name='customize_character'),
    path('character/delete/<int:character_id>/', views.delete_character, name='delete_character'), # this path is called upon cancellation of character creation
    path('character/review/<int:character_id>/', views.character_review, name='character_review'),
    path('character/updatecharacter/<int:character_id>/', views.update_character_details, name='update_character_details'),
    path('character/updatecustomization/<int:character_id>/', views.update_character_customization, name='update_character_customization'),
    path('character/<int:character_id>/pdf/', views.generate_character_pdf, name='character_pdf'),

    
    #backgrounds
    
    path('actcompendium/acolyte', views.actwiki_backgrounds_acolyte, name="actwiki_backgrounds_acolyte"),
    path('actcompendium/anthropologist', views.actwiki_backgrounds_anthropologist, name="actwiki_backgrounds_anthropologist"),
    path('actcompendium/archaeologist', views.actwiki_backgrounds_archaeologist, name="actwiki_backgrounds_archaeologist"),
    path('actcompendium/athlete', views.actwiki_backgrounds_athlete, name="actwiki_backgrounds_athlete"),
    path('actcompendium/charlatan', views.actwiki_backgrounds_charlatan, name="actwiki_backgrounds_charlatan"),
    path('actcompendium/citywatch', views.actwiki_backgrounds_citywatch, name="actwiki_backgrounds_citywatch"),
    path('actcompendium/clancrafter', views.actwiki_backgrounds_clancrafter, name="actwiki_backgrounds_clancrafter"),
    path('actcompendium/cloisteredscholar', views.actwiki_backgrounds_cloisteredscholar, name="actwiki_backgrounds_cloisteredscholar"),
    path('actcompendium/courtier', views.actwiki_backgrounds_courtier, name="actwiki_backgrounds_courtier"),
    path('actcompendium/criminal', views.actwiki_backgrounds_criminal, name="actwiki_backgrounds_criminal"),
    path('actcompendium/entertainer', views.actwiki_backgrounds_entertainer, name="actwiki_backgrounds_entertainer"),
    path('actcompendium/faceless', views.actwiki_backgrounds_faceless, name="actwiki_backgrounds_faceless"),
    path('actcompendium/factionagent', views.actwiki_backgrounds_factionagent, name="actwiki_backgrounds_factionagent"),
    path('actcompendium/fartraveler', views.actwiki_backgrounds_fartraveler, name="actwiki_backgrounds_fartraveler"),
    path('actcompendium/feylost', views.actwiki_backgrounds_feylost, name="actwiki_backgrounds_feylost"),
    path('actcompendium/fisher', views.actwiki_backgrounds_fisher, name="actwiki_backgrounds_fisher"),
    path('actcompendium/folkhero', views.actwiki_backgrounds_folkhero, name="actwiki_backgrounds_folkhero"),
    path('actcompendium/giantfoundling', views.actwiki_backgrounds_giantfoundling, name="actwiki_backgrounds_giantfoundling"),
    path('actcompendium/gladiator', views.actwiki_backgrounds_gladiator, name="actwiki_backgrounds_gladiator"),
    path('actcompendium/guildartisan', views.actwiki_backgrounds_guildartisan, name="actwiki_backgrounds_guildartisan"),
    path('actcompendium/guildmerchant', views.actwiki_backgrounds_guildmerchant, name="actwiki_backgrounds_guildmerchant"),
    path('actcompendium/hauntedone', views.actwiki_backgrounds_hauntedone, name="actwiki_backgrounds_hauntedone"),
    path('actcompendium/hermit', views.actwiki_backgrounds_hermit, name="actwiki_backgrounds_hermit"),
    path('actcompendium/houseagent', views.actwiki_backgrounds_houseagent, name="actwiki_backgrounds_houseagent"),
    path('actcompendium/inheritor', views.actwiki_backgrounds_inheritor, name="actwiki_backgrounds_inheritor"),
    path('actcompendium/investigator_scag', views.actwiki_backgrounds_investigator_scag, name="actwiki_backgrounds_investigator_scag"),
    path('actcompendium/investigator_vrgr', views.actwiki_backgrounds_investigator_vrgr, name="actwiki_backgrounds_investigator_vrgr"),
    path('actcompendium/knight', views.actwiki_backgrounds_knight, name="actwiki_backgrounds_knight"),
    path('actcompendium/knightoftheorder', views.actwiki_backgrounds_knightoftheorder, name="actwiki_backgrounds_knightoftheorder"),
    path('actcompendium/marine', views.actwiki_backgrounds_marine, name="actwiki_backgrounds_marine"),
    path('actcompendium/mercenaryveteran', views.actwiki_backgrounds_mercenaryveteran, name="actwiki_backgrounds_mercenaryveteran"),
    path('actcompendium/noble', views.actwiki_backgrounds_noble, name="actwiki_backgrounds_noble"),
    path('actcompendium/outlander', views.actwiki_backgrounds_outlander, name="actwiki_backgrounds_outlander"),
    path('actcompendium/pirate', views.actwiki_backgrounds_pirate, name="actwiki_backgrounds_pirate"),
    path('actcompendium/rewarded', views.actwiki_backgrounds_rewarded, name="actwiki_backgrounds_rewarded"),
    path('actcompendium/ruined', views.actwiki_backgrounds_ruined, name="actwiki_backgrounds_ruined"),
    path('actcompendium/runecarver', views.actwiki_backgrounds_runecarver, name="actwiki_backgrounds_runecarver"),
    path('actcompendium/sage', views.actwiki_backgrounds_sage, name="actwiki_backgrounds_sage"),
    path('actcompendium/sailor', views.actwiki_backgrounds_sailor, name="actwiki_backgrounds_sailor"),
    path('actcompendium/shipwright', views.actwiki_backgrounds_shipwright, name="actwiki_backgrounds_shipwright"),
    path('actcompendium/smuggler', views.actwiki_backgrounds_smuggler, name="actwiki_backgrounds_smuggler"),
    path('actcompendium/soldier', views.actwiki_backgrounds_soldier, name="actwiki_backgrounds_soldier"),
    path('actcompendium/spy', views.actwiki_backgrounds_spy, name="actwiki_backgrounds_spy"), 
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







