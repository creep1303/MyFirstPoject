from django.shortcuts import render
from valorant.models import Agent, Player

def home(request):
    agents = Agent.objects.all()
    players = Player.objects.all()
    return render(request, 'home.html', {'agents': agents, 'players': players})
