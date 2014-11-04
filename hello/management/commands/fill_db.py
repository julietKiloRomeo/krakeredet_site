from django.core.management.base import BaseCommand
from hello.models import User, Points, Tournament, Discipline, Standings
import datetime

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'sets up a database with default elements'

    def handle(self, *args, **options):
        Points.objects.all().delete()
        User.objects.all().delete()
        Standings.objects.all().delete()
        Tournament.objects.all().delete()
        Discipline.objects.all().delete()
        
        
        # users        
        jimbo = User(name = 'Jimmy',
                     nick = 'Jimbo',
                     description     = 'qwe' ,
                     height          = 183,
                     weight          = 90.0,
                     birthdate       = '1979-09-19',
                     email           = 'jimmy.kjaersgaard@gmail.com',
                     passwordhash    = '123',
                     country         = 'DK',
                     level           = 2)
        brede = User(name = 'Thomas',
                     nick = 'Brederen',
                     description     = 'qwe' ,
                     height          = 180,
                     weight          = 90.0,
                     birthdate       = '1983-09-19',
                     email           = 'bredesens@gmail.com',
                     passwordhash    = '124',
                     country         = 'NO',
                     level           = 4)
        jimbo.save()                     
        brede.save()                     
        
        # disciplines       
        dart = Discipline(name = 'Dart',
                          description = 'Mickey Mouse')  
        skydning = Discipline(name = 'Skydning',
                          description = 'Luftgevar')  
        dart.save()
        skydning.save()
        
        # tournaments
        comp = Tournament(name = 'Vansjo Open',
                          date = '2012-02-19')
        comp.save()
        
#        # standings
        dart_results = Standings(discipline = dart,
                                 tournament = comp)
        skyd_results = Standings(discipline = skydning,
                                 tournament = comp)
        dart_results.save()            
        skyd_results.save()            
        
        # points
        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results,
                   score = 12)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results,
                   score = 10)
        p.save()

        p = Points(points = 3, 
                   user = jimbo,
                   standings = skyd_results,
                   score = 32)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = skyd_results,
                   score = 37)
        p.save()
