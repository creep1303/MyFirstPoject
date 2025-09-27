from django import forms
from  .models import Agent, Player
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'role']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'level']
