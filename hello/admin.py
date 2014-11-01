from django.contrib import admin
from hello.models import User
from hello.models import Discipline
from hello.models import Points
from hello.models import Standings
from hello.models import Tournament
from hello.models import Post

admin.site.register(User)
admin.site.register(Discipline)
admin.site.register(Points)
admin.site.register(Standings)
admin.site.register(Tournament)
admin.site.register(Post)
