from django.shortcuts import render

from .models import Greeting

from models import User, Tournament, Standings, Discipline, Points

# Create your views here.
def index(request):
    comps = Tournament.objects.all()
    return render(request, 'index.html', {'comps': comps})

def tournament(request, idx):
    comp = Tournament.objects.get(pk=idx)
    standings = Standings.objects.filter(tournament=idx)
    tournament = {}
    # loop over disciplines
    for s in standings:
        all_p = Points.objects.filter(standings = s.pk)
        tournament[s.discipline.name]=[]
        # loop over participants
        for p in all_p:
            out = {}
            out['name'] = p.user.name
            out['score'] = p.score
            out['points'] = p.points
            tournament[s.discipline.name].append(out)
        # sort participants, most points first
    
    return render(request, 'tournament.html', {'comp': comp, 'tournament':tournament})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


