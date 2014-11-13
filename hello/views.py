from django.shortcuts import render
from django.db.models import Avg
from .models import Greeting

from models import User, Tournament, Standings, Discipline, Points

# Create your views here.
def index(request):
    comps = Tournament.objects.all()
    return render(request, 'index.html', {'comps': comps})

def tournament_list(request):
    comps = Tournament.objects.all()
    return render(request, 'tournament_list.html', {'comps': comps})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def discipline_list(request):
    disciplines = Discipline.objects.all()
    return render(request, 'discipline_list.html', {'disciplines': disciplines})

def user_detail(request, idx):
    # fetch user
    users = User.objects.all()
    this_user = User.objects.get(pk=idx)
    # init best results
    best_results = {}
    avg_pts = []
    records = {}
    # populate best results
    disciplines = Discipline.objects.all()
    for d in disciplines:
        disc_query = Points.objects.filter(user=this_user).filter(standings__discipline=d)
        best_results[d.name] = disc_query.order_by('-score')[0:3]
        records[d.name] = d.record()
        disc_avg = disc_query.aggregate(Avg('points'))
        avg_pts.append({ 'discipline':d.name, 'avg_pts': disc_avg['points__avg'] })
    # populate tournament placements
    comps = Tournament.objects.filter(standings__points__user=this_user).distinct()
    wins = [0,0]
    for c in comps:
        wins[1] += 1
        comp_podium = c.totals()['total']
        winner = max(comp_podium, key=lambda x:x['points'])
        if winner['name']==this_user.name:
            wins[0] += 1
    
    return render(request, 'user_detail.html', {'user': this_user, 'results':best_results, 'wins':wins, 'avg_pts':avg_pts, 'users': users, 'records': records})

def tournament_detail(request, idx):
    # fetch tournament
    comp = Tournament.objects.get(pk=idx)
    # retrieve dict with standings in eacg discipline as well as totals
    standings = comp.totals()
    comps = Tournament.objects.all()
    
    return render(request, 'tournament_detail.html', {'comp': comp, 'standings':standings,'comps': comps})
    
def discipline_detail(request, idx):
    disc = Discipline.objects.get(pk=idx)
    disciplines = Discipline.objects.all()
    # get list of top 5 scores ever
    top_5 = Points.objects.filter(standings__discipline=disc).order_by('-score')[0:5]    
    
    return render(request, 'discipline_detail.html',{'discipline':disc, 'top_5':top_5, 'disciplines':disciplines})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
