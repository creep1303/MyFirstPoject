from django.shortcuts import render,redirect
from .forms import AgentForm
from .forms import PlayerForm
from .models import Agent
from .models import Player
def create_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AgentForm()
        return render(request, 'form.html', {'form': form})

def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlayerForm()
        return render(request, 'form.html', {'form': form})

def update_player(request,b_id):
    player = Player.objects.get(id=b_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlayerForm()
        return render(request, 'form.html', {'form': form})


def update_agent(request,b_id):
    agent = Agent.objects.get(id=b_id)
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AgentForm()
        return render(request, 'form.html', {'form': form})