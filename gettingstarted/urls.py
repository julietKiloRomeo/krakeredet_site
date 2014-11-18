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
    url(r'^tournament/([0-9]*?)/$', hello.views.tournament_detail),
    url(r'^tournament/$', hello.views.tournament_list),
    url(r'^user/(.*?)/$', hello.views.user_detail),
    url(r'^user/$', hello.views.user_list),
    url(r'^discipline/(.*?)/$', hello.views.discipline_detail),
    url(r'^discipline/$', hello.views.discipline_list),
#    url(r'^register/$', hello.views.register),
    url(r'^login/$', hello.views.user_login),
    url(r'^logout/$', hello.views.user_logout),
    url(r'^profile/(.*?)/$', hello.views.profile_detail),

)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
