from django.contrib import admin
from .models import Hackathon
from .forms import TeamChangeListForm
from django.contrib.admin.views.main import ChangeList

class TeamChangeList(ChangeList):
	def __init__(self, request, model, list_display, list_display_links, list_filter, date_hierarchy, search_fields, list_select_related, list_per_page, list_max_show_all, list_editable, model_admin):

		super(TeamChangeList, self).__init__(request, model,
			list_display, list_display_links, list_filter,
			date_hierarchy, search_fields, list_select_related,
			list_per_page, list_max_show_all, list_editable, 
			model_admin)
		
		self.list_display = ['action_checkbox', 'hackathon_name', 'hackathon_team_going']
		self.list_display_links = ['hackathon_name']
		self.list_editable = ['hackathon_team_going']

class TeamAdmin(admin.ModelAdmin):
	def get_changelist(self, request, **kwargs):
		return TeamChangeList

	def get_changelist_form(self, request, **kwargs):
		return TeamChangeListForm

admin.site.register(Hackathon)