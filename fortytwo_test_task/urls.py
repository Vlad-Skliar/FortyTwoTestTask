from django.conf.urls import patterns, include, url

from django.contrib import admin

from apps.info import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.InfoDetailView.as_view(), name='info'),
    url(r'^admin/', include(admin.site.urls)),
)
