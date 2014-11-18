from django.shortcuts import render, render_to_response
from django.db.models import Avg
#from hello.forms import UserForm, ProfileForm
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from models import Profile, Tournament, Discipline, Points, Fish

# Create your views here.
def index(request):
    comps = Tournament.objects.all()
    return render(request, 'index.html', {'request':request,
                                          'comps': comps})

def tournament_list(request):
    comps = Tournament.objects.all()
    return render(request, 'tournament_list.html', {'request':request,
                                                    'comps': comps})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'request':request,
                                              'users': users,
                                              'N':len(users)})

def discipline_list(request):
    disciplines = Discipline.objects.all()
    return render(request, 'discipline_list.html', {'request':request,
                                                    'disciplines': disciplines})
def fish_list(request):
    fishes = Fish.objects.all()
    return render(request, 'fish_list.html', {'request':request,
                                              'fishes': fishes})

def user_detail(request, username):
    # fetch user
    users = User.objects.all()
    this_user = Profile.objects.get(user__username=username)
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
        if winner['name']==this_user.user.first_name:
            wins[0] += 1
    
    return render(request, 'user_detail.html', {'request':request,
                                                'user': this_user, 
                                                'results':best_results, 
                                                'wins':wins, 
                                                'avg_pts':avg_pts, 
                                                'users': users, 
                                                'records': records})

def tournament_detail(request, idx):
    # fetch tournament
    comp = Tournament.objects.get(pk=idx)
    # retrieve dict with standings in eacg discipline as well as totals
    standings = comp.totals()
    comps = Tournament.objects.all()
    
    return render(request, 'tournament_detail.html', {'request':request,
                                                      'comp': comp, 
                                                      'standings':standings,
                                                      'comps': comps})
    
def discipline_detail(request, name):
    disc = Discipline.objects.get(name__iexact=name)
    disciplines = Discipline.objects.all()
    # get list of top 5 scores ever
    top_5 = Points.objects.filter(standings__discipline=disc).order_by('-score')[0:5]    
    
    return render(request, 'discipline_detail.html',{'request':request,
                                                     'discipline':disc, 
                                                     'top_5':top_5, 
                                                     'disciplines':disciplines})


def fish_detail(request, idx):
    fish = Fish.objects.get(pk=idx)
    
    return render(request, 'fish_detail.html',{'request':request,
                                                     'fish':fish})












#def register(request):
#    # Like before, get the request's context.
#    context = RequestContext(request)
#
#    # A boolean value for telling the template whether the registration was successful.
#    # Set to False initially. Code changes value to True when registration succeeds.
#    registered = False
#
#    # If it's a HTTP POST, we're interested in processing form data.
#    if request.method == 'POST':
#        # Attempt to grab information from the raw form information.
#        # Note that we make use of both UserForm and UserProfileForm.
#        user_form = UserForm(data=request.POST)
#        profile_form = ProfileForm(data=request.POST)
#
#        # If the two forms are valid...
#        if user_form.is_valid() and profile_form.is_valid():
#            # Save the user's form data to the database.
#            user = user_form.save()
#
#            # Now we hash the password with the set_password method.
#            # Once hashed, we can update the user object.
#            user.set_password(user.password)
#            user.save()
#
#            # Now sort out the UserProfile instance.
#            # Since we need to set the user attribute ourselves, we set commit=False.
#            # This delays saving the model until we're ready to avoid integrity problems.
#            profile = profile_form.save(commit=False)
#            profile.user = user
#
#            # Did the user provide a profile picture?
#            # If so, we need to get it from the input form and put it in the UserProfile model.
#            if 'image' in request.FILES:
#                profile.image = request.FILES['image']
#
#            # Now we save the UserProfile model instance.
#            profile.save()
#
#            # Update our variable to tell the template registration was successful.
#            registered = True
#
#        # Invalid form or forms - mistakes or something else?
#        # Print problems to the terminal.
#        # They'll also be shown to the user.
#        else:
#            print user_form.errors, profile_form.errors
#
#    # Not a HTTP POST, so we render our form using two ModelForm instances.
#    # These forms will be blank, ready for user input.
#    else:
#        user_form = UserForm()
#        profile_form = ProfileForm()
#
#    # Render the template depending on the context.
#    return render_to_response(
#            'register.html',
#            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
#            context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)


@login_required
def profile_detail(request, name):
    prof = Profile.objects.get(user__username = name)
    if prof == request.user.profile:
        return render(request, 'profile.html',{'request':request,'profile':prof})
    else:
        return HttpResponse("You are not authorized to view this page.")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

        