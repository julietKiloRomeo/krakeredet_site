from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    

class User(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    name            = models.CharField(max_length=200)
    nick            = models.CharField(max_length=200)
    image           = models.ImageField(upload_to='/media/', blank=True, null=True)
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
    
class Discipline(models.Model):
    created     = models.DateTimeField('date created', auto_now_add=True)
    name        = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='/media/', blank=True, null=True)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Points(models.Model):
    user    = models.ForeignKey(User)
    points  = models.IntegerField()

class Standings(models.Model):
    discipline = models.ForeignKey(Discipline)

class Tournament(models.Model):
    created                 = models.DateTimeField('date created', auto_now_add=True)
    name                    = models.CharField(max_length=200)
    date                    = models.DateField()
    discipline_standings    = models.ForeignKey(Standings)
    def __unicode__(self):
        return self.date

class Post(models.Model):
    text    = models.TextField()
    user    = models.ForeignKey(User)
    time    = models.DateTimeField()
    parent  = models.ForeignKey('self')