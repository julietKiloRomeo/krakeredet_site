from django.shortcuts import render

from .models import Greeting

from models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


