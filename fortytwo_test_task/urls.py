from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.testapp import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.test_view, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
