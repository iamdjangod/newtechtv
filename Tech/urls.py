"""
Definition of urls for Tech.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from registration.backends.simple.views import RegistrationView

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^tech0t5v2m0a1r5k1e242m/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^tech0t5v2m0a1r5k1e242m/', include('registration.backends.simple.urls')),
    (r'^techv1d2e4o6s0t5v2m0a1r5k1e242m/', include('django_youtube.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
