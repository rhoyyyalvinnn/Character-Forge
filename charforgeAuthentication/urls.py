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
]