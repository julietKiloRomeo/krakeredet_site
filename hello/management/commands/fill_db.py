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
        kroket = Discipline(name = 'Kroket',
                          description = 'Vansjo rules')  
        dart.save()
        skydning.save()
        kroket.save()
        
        # tournaments
        comp1 = Tournament(name = 'Vansjo Open',
                          date = '2012-02-19')
        comp1.save()

        comp2 = Tournament(name = 'Vansjo Open',
                          date = '2011-02-19')
        comp2.save()
        
#        # standings
        dart_results1 = Standings(discipline = dart,
                                 tournament = comp1)
        skyd_results1 = Standings(discipline = skydning,
                                 tournament = comp1)
        krok_results1 = Standings(discipline = kroket,
                                 tournament = comp1)
        dart_results1.save()            
        skyd_results1.save()            
        krok_results1.save()            

        dart_results2 = Standings(discipline = dart,
                                 tournament = comp2)
        skyd_results2 = Standings(discipline = skydning,
                                 tournament = comp2)
        krok_results2 = Standings(discipline = kroket,
                                 tournament = comp2)
        dart_results2.save()            
        skyd_results2.save()            
        krok_results2.save()            
        
        # points
        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results1,
                   score = 12)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results1,
                   score = 10)
        p.save()

        p = Points(points = 3, 
                   user = jimbo,
                   standings = skyd_results1,
                   score = 32)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = skyd_results1,
                   score = 37)
        p.save()

        p = Points(points = 0, 
                   user = jimbo,
                   standings = krok_results1,
                   score = 5)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results1,
                   score = 100)
        p.save()
        #----------
        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results2,
                   score = 12)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results2,
                   score = 10)
        p.save()

        p = Points(points = 3, 
                   user = jimbo,
                   standings = skyd_results2,
                   score = 32)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = skyd_results2,
                   score = 37)
        p.save()

        p = Points(points = 0, 
                   user = jimbo,
                   standings = krok_results2,
                   score = 5)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results2,
                   score = 100)
        p.save()




