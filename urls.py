from testdeals.deals import views

from django.conf.urls.defaults import *

# Required to make static serving work
from django.conf import settings
from django.views.static import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
	
    (r'^$', views.home),
	(r'^about_us/$', views.about_us),
	(r'^contact_us/$', views.contact_us),
)

if settings.DEBUG == True:
	# Required to make static serving work
	urlpatterns += patterns('',
			(r'^staticmedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
			)
