from django.db import models
from django.core.cache import cache

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    

class User(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    name            = models.CharField(max_length=200)
    nick            = models.CharField(max_length=200)
    image           = models.ImageField(upload_to='.', blank=True, null=True)
    description     = models.TextField()
    height          = models.IntegerField()
    weight          = models.FloatField()
    birthdate       = models.DateField()
    email           = models.EmailField()
    passwordhash    = models.CharField(max_length=200)
    country         = models.CharField(max_length=200)
    level           = models.IntegerField()
    
    
    def __unicode__(self):
        return self.name
    def level_name(self):
        names = [u'Kj\xf8tmeis',u'Kr\xe5ke',u'\xd8rn',u'F\xf8nix']
        return names[self.level - 1]
    
class Discipline(models.Model):
    created     = models.DateTimeField('date created', auto_now_add=True)
    name        = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='.', blank=True, null=True)
    description = models.TextField()
    def __unicode__(self):
        return self.name


class Tournament(models.Model):
    created                 = models.DateTimeField('date created', auto_now_add=True)
    name                    = models.CharField(max_length=200)
    date                    = models.DateField()
    def __unicode__(self):
        return self.name + ' ' + self.date.strftime('%d %B %y')
        
    def totals(self):
        
        
        cache_key = 'comp_totals' + str(self.pk)
        cache_time = 1800 # time to live in seconds
        tournament = cache.get(cache_key)
        if not tournament:
            standings = Standings.objects.filter(tournament=self)
            # init dict for tournament data
            tournament = {}
            # init total field
            tournament['total']={}
            # loop over disciplines and populate tournament
            for s in standings:
                # find all Point objects in standings
                all_p = Points.objects.filter(standings = s).order_by('-points')
                # and int a dict for this discipline
                tournament[s.discipline.name]=[]
                # loop over participants
                for p in all_p:
                    # put participants score in discipline field
                    tournament[s.discipline.name].append({'points':p.points,'score':p.score, 'pk':p.user.pk, 'name':p.user.name})
                    # also add points in this discipline to totals
                    if p.user.name in tournament['total'].keys():
                        tournament['total'][p.user.name]['points'] += p.points 
                    else:
                        tournament['total'][p.user.name] = {'points':p.points}
                        tournament['total'][p.user.name]['points'] = p.points 
            tmp = []
            for name in tournament['total'].keys():
                tmp.append({'points':tournament['total'][name]['points'], 'name':name})
            tournament['total'] = tmp
            cache.set(cache_key, tournament, cache_time)

        return tournament

class Standings(models.Model):
    discipline = models.ForeignKey(Discipline)
    tournament = models.ForeignKey(Tournament)
    class Meta:
        verbose_name_plural = "standings"

class Points(models.Model):
    user        = models.ForeignKey(User)
    standings   = models.ForeignKey(Standings)
    points      = models.IntegerField()
    score       = models.IntegerField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "points"

class Post(models.Model):
    text    = models.TextField()
    user    = models.ForeignKey(User)
    time    = models.DateTimeField()
    parent  = models.ForeignKey('self')