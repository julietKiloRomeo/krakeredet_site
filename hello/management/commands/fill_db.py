from django.core.management.base import BaseCommand
from hello.models import Profile, Points, Tournament, Discipline, Standings
from django.contrib.auth.models import User

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
        jimbo = User.objects.get(name='jkr')        
        jimbo_prof = User(nick = 'Jimbo',
                     description     = 'qwe' ,
                     height          = 183,
                     weight          = 90.0,
                     birthdate       = '1979-09-19',
                     country         = 'DK',
                     level           = 2,
                     user            = jimbo)
        jimbo_prof.save()

        jimbo = User.objects.create_user('Jimmy', 'jimmy.kjaersgaard@gmail.com', 'eskadron')        
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
        tombo = User(name = 'Tommy',
                     nick = 'Bro',
                     description     = 'rty' ,
                     height          = 200,
                     weight          = 100.0,
                     birthdate       = '1983-06-14',
                     email           = 'tommy.rasmussen@gmail.com',
                     passwordhash    = '124',
                     country         = 'DK',
                     level           = 2)
        jon     = User(name = 'Jon',
                     nick = '',
                     description     = 'as ety f gn' ,
                     height          = 180,
                     weight          = 80.0,
                     birthdate       = '1983-07-14',
                     email           = 'jon@pagh.com',
                     passwordhash    = '124',
                     country         = 'DK',
                     level           = 3)
        jimbo.save()                     
        brede.save()                     
        tombo.save()                     
        jon.save()                     
        
        # disciplines       
        dart = Discipline(name = 'Dart',
                          description = 'Mickey Mouse')  
        skydning = Discipline(name = 'Skydning',
                          description = 'Luftgevar')  
        kroket = Discipline(name = 'Kroket',
                          description = 'Vansjo rules')  
        poker  = Discipline(name = 'Poker',
                          description = "Hold 'Em")  
        dart.save()
        skydning.save()
        kroket.save()
        poker.save()
        
        # tournaments
        comp1 = Tournament(name = 'Vansjo Open',
                          date = '2012-02-19')
        comp1.save()

        comp2 = Tournament(name = 'Vansjo Open',
                          date = '2011-02-19')
        comp2.save()

        comp3 = Tournament(name = 'Vansjo Open',
                          date = '2013-03-19')
        comp3.save()
        
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
        
        dart_results3 = Standings(discipline = dart,
                                 tournament = comp3)
        skyd_results3 = Standings(discipline = skydning,
                                 tournament = comp3)
        krok_results3 = Standings(discipline = kroket,
                                 tournament = comp3)
        dart_results3.save()            
        skyd_results3.save()            
        krok_results3.save()            
        # points
        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results1,
                   score = 14)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results1,
                   score = 10)
        p.save()
        p = Points(points = 2, 
                   user = tombo,
                   standings = dart_results1,
                   score = 8)
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
        p = Points(points = 2, 
                   user = tombo,
                   standings = skyd_results1,
                   score = 30)
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
        p = Points(points = 3, 
                   user = tombo,
                   standings = krok_results1,
                   score = 71)
        p.save()
        #----------
        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results2,
                   score = 12)
        p.save()
        p = Points(points = 2, 
                   user = brede,
                   standings = dart_results2,
                   score = 6)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = dart_results2,
                   score = 11)
        p.save()

        p = Points(points = 2, 
                   user = jimbo,
                   standings = skyd_results2,
                   score = 31)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = skyd_results2,
                   score = 39)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = skyd_results2,
                   score = 32)
        p.save()

        p = Points(points = 0, 
                   user = jimbo,
                   standings = krok_results2,
                   score = 4)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results2,
                   score = 107)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = krok_results2,
                   score = 87)
        p.save()

        #----------
        p = Points(points = 2, 
                   user = jimbo,
                   standings = dart_results3,
                   score = 11)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results3,
                   score = 9)
        p.save()
        p = Points(points = 4, 
                   user = tombo,
                   standings = dart_results3,
                   score = 17)
        p.save()

        p = Points(points = 2, 
                   user = jimbo,
                   standings = skyd_results3,
                   score = 35)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = skyd_results3,
                   score = 41)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = skyd_results3,
                   score = 34)
        p.save()

        p = Points(points = 0, 
                   user = jimbo,
                   standings = krok_results3,
                   score = 42)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results3,
                   score = 105)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = krok_results3,
                   score = 91)
        p.save()
