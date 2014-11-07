from django.db import models


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