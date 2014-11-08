from django.shortcuts import render

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
    this_user = User.objects.get(pk=idx)
    # init best results
    best_results = {}
    # populate best results
    disciplines = Discipline.objects.all()
    for d in disciplines:
        best_results[d.name] = Points.objects.filter(user=this_user).filter(standings__discipline=d).order_by('-score')[0:3]
    
    return render(request, 'user_detail.html', {'user': this_user, 'results':best_results})

def tournament_detail(request, idx):
    # fetch tournament
    comp = Tournament.objects.get(pk=idx)
    # and corresponding standings
    standings = Standings.objects.filter(tournament=idx)
    # init dict for tournament data
    tournament = {}
    # init temporary dict for total score
    total = {}
    # loop over disciplines and populate tournament and totals
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
        # reorder totals for use with django's dictsort filter
        for name in total.keys():
            pts  = total[name]
            total_list.append({'name':name, 'points':pts})
        # sort participants, most points first
    
    return render(request, 'tournament_detail.html', {'comp': comp, 'tournament':tournament, 'total':total_list})
    
    
def discipline_detail(request, idx):
    disc = Discipline.objects.get(pk=idx)
    # get list of top 5 scores ever
    top_5 = Points.objects.filter(standings__discipline=disc).order_by('-score')[0:5]    
    
    return render(request, 'discipline_detail.html',{'discipline':disc, 'top_5':top_5})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


