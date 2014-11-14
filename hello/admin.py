from django.contrib import admin
from hello.models import Profile
from hello.models import Discipline
from hello.models import Points
from hello.models import Standings
from hello.models import Tournament
from hello.models import Post


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Discipline)
admin.site.register(Points)
admin.site.register(Standings)
admin.site.register(Tournament)
admin.site.register(Post)
