from django.shortcuts import render

from .models import Greeting

from models import User, Tournament, Standings

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def tournament(request, idx):
    comp = Tournament.objects.get(pk=idx)
    standings = Standings.objects.filter(tournament=idx)
    
    return render(request, 'tournament.html', {'comp': comp, 'standings':standings})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


