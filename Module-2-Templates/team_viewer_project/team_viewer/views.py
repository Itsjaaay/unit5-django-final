# team_viewer/views.py
from django.shortcuts import render
from .models import Team

def team_list(request):
    teams = {
        'management': Team(name='Management', description='Management Team', members=['John', 'Jane']),
        'procurement': Team(name='Procurement', description='Procurement Team', members=['Bob', 'Alice']),
        'community': Team(name='community', description='Community Team', members=['Bob', 'Alice']),
        'documentation': Team(name='documentation', description='Documentation Team', members=['Bob', 'Alice']),
        # Add other teams here
    }
    return render(request, 'team_viewer/team_list.html', {'teams': teams})
