from django.contrib import admin

# Register your models here.

from .models import Agent
from .models import Player

admin.site.register(Agent)
admin.site.register(Player)