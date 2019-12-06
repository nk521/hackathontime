from django import forms
from hackathontime_users.models import Team


class TeamChangeListForm(forms.ModelForm):
    hackathon_team_going = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(), required=False)