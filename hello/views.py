from django.shortcuts import render

from .models import Greeting

from models import User, Tournament, Standings, Discipline, Points

# Create your views here.
def index(request):
    comps = Tournament.objects.all()
    return render(request, 'index.html', {'comps': comps})

def user_detail(request, idx):
    this_user = User.objects.get(pk=idx)
    
    best_results = {}
    
    disciplines = Discipline.objects.all()
    for d in disciplines:
        best_results[d.name] = Points.objects.filter(user=this_user).filter(standings__discipline=d).order_by('-score')[0:3]
    
    
    return render(request, 'user_detail.html', {'user': this_user, 'results':best_results})

def tournament(request, idx):
    comp = Tournament.objects.get(pk=idx)
    standings = Standings.objects.filter(tournament=idx)
    tournament = {}
    total = {}
    # loop over disciplines
    for s in standings:
        all_p = Points.objects.filter(standings = s).order_by('-points')
        tournament[s.discipline.name]=[]
        # loop over participants
        for p in all_p:
            tournament[s.discipline.name].append(p)
            if p.user.name in total:
                total[p.user.name] += p.points 
            else:
                total[p.user.name] = p.points
        total_list = []
        for name in total.keys():
            pts  = total[name]
            total_list.append({'name':name, 'points':pts})
        # sort participants, most points first
    
    return render(request, 'tournament.html', {'comp': comp, 'tournament':tournament, 'total':total_list})
    
    
def discipline_detail(request, idx):
    disc = Discipline.objects.get(pk=idx)
    return render(request, 'discipline_detail.html',{'discipline':disc})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


