from django.core.management.base import BaseCommand
from hello.models import Points, Tournament, Discipline, Standings, Fish
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'sets up a database with default elements'

    def handle(self, *args, **options):
        Fish.objects.all().delete()
        Points.objects.all().delete()
        Standings.objects.all().delete()
        Discipline.objects.all().delete()
        Tournament.objects.all().delete()
        
        
        # disciplines       
        dart = Discipline(name = 'Dart',
                          description = 'Mickey Mouse')  
        skydning = Discipline(name = 'Skydning',
                          description = 'Luftgevar')  
        kroket = Discipline(name = 'Kroket',
                          description = 'Vansjo rules')  
        poker  = Discipline(name = 'Poker',
                          description = "Hold 'Em")  
        fiskning  = Discipline(name = 'Fiskning',
                          description = ".d.d.")  
        dart.save()
        skydning.save()
        kroket.save()
        poker.save()
        fiskning.save()
        
        
#        dart     = Discipline.objects.get(name='Dart')        
#        skydning = Discipline.objects.get(name='Skydning')        
#        kroket   = Discipline.objects.get(name='Kroket')        
        
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


        jimbo = User.objects.get(username = 'jkr')
        brede = User.objects.get(username = 'tbr')
        tombo = User.objects.get(username = 'tkr')
        pagh  = User.objects.get(username = 'jpa')


        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results1)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results1)
        p.save()
        p = Points(points = 2, 
                   user = tombo,
                   standings = dart_results1)
        p.save()
        p = Points(points = 1, 
                   user = pagh,
                   standings = dart_results1)
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
                   standings = krok_results1)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results1)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = krok_results1)
        p.save()
        p = Points(points = 2, 
                   user = pagh,
                   standings = krok_results1)
        p.save()
        #----------
        p = Points(points = 4, 
                   user = jimbo,
                   standings = dart_results2)
        p.save()
        p = Points(points = 2, 
                   user = brede,
                   standings = dart_results2)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = dart_results2)
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
                   standings = krok_results2)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results2)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = krok_results2)
        p.save()

        #----------
        p = Points(points = 2, 
                   user = jimbo,
                   standings = dart_results3)
        p.save()
        p = Points(points = 3, 
                   user = brede,
                   standings = dart_results3)
        p.save()
        p = Points(points = 4, 
                   user = tombo,
                   standings = dart_results3)
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
                   standings = krok_results3)
        p.save()
        p = Points(points = 4, 
                   user = brede,
                   standings = krok_results3)
        p.save()
        p = Points(points = 3, 
                   user = tombo,
                   standings = krok_results3)
        p.save()
