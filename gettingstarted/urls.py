from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^turnering/([0-9]*?)/$', hello.views.tournament_detail),
    url(r'^turnering/$', hello.views.tournament_list),
    url(r'^bruker/(.*?)/$', hello.views.user_detail),
    url(r'^bruker/$', hello.views.user_list),
    url(r'^disiplin/(.*?)/$', hello.views.discipline_detail),
    url(r'^disiplin/$', hello.views.discipline_list),
#    url(r'^register/$', hello.views.register),
    url(r'^login/$', hello.views.user_login),
    url(r'^logout/$', hello.views.user_logout),
    url(r'^profil/(.*?)/$', hello.views.profile_detail),
    url(r'^fisk/$', hello.views.fish_list),
    url(r'^fisk/([0-9]*?)/$', hello.views.fish_detail),
    url(r'^ny_fisk/$', hello.views.add_fish),

)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
