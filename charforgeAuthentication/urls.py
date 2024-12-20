from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('gamerules', views.gamerules, name="gamerules"),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('community', views.community, name='community'),
    path('forum', views.forum, name='forum'),
    
    
    path('compendium/', views.compendium, name="compendium"),
    
    path('compendium/artificer', views.wiki_spells_artificer, name="wiki_spells_artificer"),
    path('compendium/bard', views.wiki_spells_bard, name="wiki_spells_bard"),
    path('compendium/cleric', views.wiki_spells_cleric, name="wiki_spells_cleric"),
    path('compendium/druid', views.wiki_spells_druid, name="wiki_spells_druid"),
    path('compendium/paladin', views.wiki_spells_paladin, name="wiki_spells_paladin"),
    path('compendium/ranger', views.wiki_spells_ranger, name="wiki_spells_ranger"),
    path('compendium/sorcerer', views.wiki_spells_sorcerer, name="wiki_spells_sorcerer"),
    path('compendium/warlock', views.wiki_spells_warlock, name="wiki_spells_warlock"),
    path('compendium/wizard', views.wiki_spells_wizard, name="wiki_spells_wizard"),
    path('compendium/dragonborn', views.wiki_lineages_dragonborn, name="wiki_lineages_dragonborn"),
    path('compendium/elf', views.wiki_lineages_elf, name="wiki_lineages_elf"),
    path('compendium/gnome', views.wiki_lineages_gnome, name="wiki_lineages_gnome"),
    path('compendium/halfelf', views.wiki_lineages_halfelf, name="wiki_lineages_halfelf"),
    path('compendium/halforc', views.wiki_lineages_halforc, name="wiki_lineages_halforc"),
    path('compendium/halfling', views.wiki_lineages_halfling, name="wiki_lineages_halfling"),
    path('compendium/human', views.wiki_lineages_human, name="wiki_lineages_human"),
    path('compendium/tiefling', views.wiki_lineages_tiefling, name="wiki_lineages_tiefling"),
    path('compendium/dwarf', views.wiki_lineages_dwarf, name="wiki_lineages_dwarf"),
    
    path('compendium/acolyte', views.wiki_backgrounds_acolyte, name="wiki_backgrounds_acolyte"),
    path('compendium/anthropologist', views.wiki_backgrounds_anthropologist, name="wiki_backgrounds_anthropologist"),
    path('compendium/archaeologist', views.wiki_backgrounds_archaeologist, name="wiki_backgrounds_archaeologist"),
    path('compendium/athlete', views.wiki_backgrounds_athlete, name="wiki_backgrounds_athlete"),
    path('compendium/charlatan', views.wiki_backgrounds_charlatan, name="wiki_backgrounds_charlatan"),
    path('compendium/citywatch', views.wiki_backgrounds_citywatch, name="wiki_backgrounds_citywatch"),
    path('compendium/clancrafter', views.wiki_backgrounds_clancrafter, name="wiki_backgrounds_clancrafter"),
    path('compendium/cloisteredscholar', views.wiki_backgrounds_cloisteredscholar, name="wiki_backgrounds_cloisteredscholar"),
    path('compendium/courtier', views.wiki_backgrounds_courtier, name="wiki_backgrounds_courtier"),
    path('compendium/criminal', views.wiki_backgrounds_criminal, name="wiki_backgrounds_criminal"),
    path('compendium/entertainer', views.wiki_backgrounds_entertainer, name="wiki_backgrounds_entertainer"),
    path('compendium/faceless', views.wiki_backgrounds_faceless, name="wiki_backgrounds_faceless"),
    path('compendium/factionagent', views.wiki_backgrounds_factionagent, name="wiki_backgrounds_factionagent"),
    path('compendium/fartraveler', views.wiki_backgrounds_fartraveler, name="wiki_backgrounds_fartraveler"),
    path('compendium/feylost', views.wiki_backgrounds_feylost, name="wiki_backgrounds_feylost"),
    path('compendium/fisher', views.wiki_backgrounds_fisher, name="wiki_backgrounds_fisher"),
    path('compendium/folkhero', views.wiki_backgrounds_folkhero, name="wiki_backgrounds_folkhero"),
    path('compendium/giantfoundling', views.wiki_backgrounds_giantfoundling, name="wiki_backgrounds_giantfoundling"),
    path('compendium/gladiator', views.wiki_backgrounds_gladiator, name="wiki_backgrounds_gladiator"),
    path('compendium/guildartisan', views.wiki_backgrounds_guildartisan, name="wiki_backgrounds_guildartisan"),
    path('compendium/guildmerchant', views.wiki_backgrounds_guildmerchant, name="wiki_backgrounds_guildmerchant"),
    path('compendium/hauntedone', views.wiki_backgrounds_hauntedone, name="wiki_backgrounds_hauntedone"),
    path('compendium/hermit', views.wiki_backgrounds_hermit, name="wiki_backgrounds_hermit"),
    path('compendium/houseagent', views.wiki_backgrounds_houseagent, name="wiki_backgrounds_houseagent"),
    path('compendium/inheritor', views.wiki_backgrounds_inheritor, name="wiki_backgrounds_inheritor"),
    path('compendium/investigator_scag', views.wiki_backgrounds_investigator_scag, name="wiki_backgrounds_investigator_scag"),
    path('compendium/investigator_vrgr', views.wiki_backgrounds_investigator_vrgr, name="wiki_backgrounds_investigator_vrgr"),
    path('compendium/knight', views.wiki_backgrounds_knight, name="wiki_backgrounds_knight"),
    path('compendium/knightoftheorder', views.wiki_backgrounds_knightoftheorder, name="wiki_backgrounds_knightoftheorder"),
    path('compendium/marine', views.wiki_backgrounds_marine, name="wiki_backgrounds_marine"),
    path('compendium/mercenaryveteran', views.wiki_backgrounds_mercenaryveteran, name="wiki_backgrounds_mercenaryveteran"),
    path('compendium/noble', views.wiki_backgrounds_noble, name="wiki_backgrounds_noble"),
    path('compendium/outlander', views.wiki_backgrounds_outlander, name="wiki_backgrounds_outlander"),
    path('compendium/pirate', views.wiki_backgrounds_pirate, name="wiki_backgrounds_pirate"),
    path('compendium/rewarded', views.wiki_backgrounds_rewarded, name="wiki_backgrounds_rewarded"),
    path('compendium/ruined', views.wiki_backgrounds_ruined, name="wiki_backgrounds_ruined"),
    path('compendium/runecarver', views.wiki_backgrounds_runecarver, name="wiki_backgrounds_runecarver"),
    path('compendium/sage', views.wiki_backgrounds_sage, name="wiki_backgrounds_sage"),
    path('compendium/sailor', views.wiki_backgrounds_sailor, name="wiki_backgrounds_sailor"),
    path('compendium/shipwright', views.wiki_backgrounds_shipwright, name="wiki_backgrounds_shipwright"),
    path('compendium/smuggler', views.wiki_backgrounds_smuggler, name="wiki_backgrounds_smuggler"),
    path('compendium/soldier', views.wiki_backgrounds_soldier, name="wiki_backgrounds_soldier"),
    path('compendium/spy', views.wiki_backgrounds_spy, name="wiki_backgrounds_spy"),
]