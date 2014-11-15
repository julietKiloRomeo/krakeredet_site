from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

class Profile(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    nick            = models.CharField(max_length=200)
    image           = models.ImageField(upload_to='./media/', blank=True, null=True)
    description     = models.TextField()
    height          = models.IntegerField()
    weight          = models.FloatField()
    birthdate       = models.DateField()
    country         = models.CharField(max_length=200)
    level           = models.IntegerField()
    user            = models.OneToOneField(User)
    
    
    def __unicode__(self):
        return self.user.first_name
    def level_name(self):
        names = [u'Kj\xf8tmeis',u'Kr\xe5ke',u'\xd8rn',u'F\xf8nix']
        return names[self.level - 1]
    
class Discipline(models.Model):
    created     = models.DateTimeField('date created', auto_now_add=True)
    name        = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='./media/', blank=True, null=True)
    description = models.TextField()
    def __unicode__(self):
        return self.name

    def record(self):
        cache_key = 'disc_record' + str(self.pk)
        cache_time = 1800 # time to live in seconds
        record = cache.get(cache_key)
        if not record:
            best_point = Points.objects.filter(standings__discipline = self).order_by('-score')
            if best_point:
                record = best_point[0].score
            else:
                record = 1
            cache.set(cache_key, record, cache_time)

        return record





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
                    tournament[s.discipline.name].append({'points':p.points,'score':p.score, 'pk':p.user.pk, 'name':p.user.first_name, 'disc':s.discipline})
                    # also add points in this discipline to totals
                    if p.user.first_name in tournament['total'].keys():
                        tournament['total'][p.user.first_name]['points'] += p.points 
                    else:
                        tournament['total'][p.user.first_name] = {'points':p.points}
                        tournament['total'][p.user.first_name]['points'] = p.points 
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