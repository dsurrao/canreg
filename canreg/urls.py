"""canreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


from . import views
from pathology import views as pathology_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^patients/$', views.IndexView.as_view(), name='patients'),
    url(r'^patients/(?P<pk>[0-9]+)/$', views.DetailView.as_view()),
    url(r'^prelim_qns/(?P<patient_id>[0-9]+)/$', views.prelim_qns),
    url(r'^curative/(?P<patient_id>[0-9]+)/$', views.curative),
    url(r'^palliative/(?P<patient_id>[0-9]+)/$', views.palliative),
    url(r'^biopsy_status/(?P<patient_id>[0-9]+)/$',
        pathology_views.biopsy_status, name='biopsy_status'),
    url(r'^biopsy/(?P<pathology_id>[0-9]+)/$', pathology_views.biopsy,
        name='biopsy'),
    url(r'^no_biopsy/(?P<pathology_id>[0-9]+)/$', pathology_views.no_biopsy,
        name='no_biopsy'),
    url(r'^scheduled_biopsy/(?P<pathology_id>[0-9]+)/$',
        pathology_views.scheduled_biopsy, name='scheduled_biopsy'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
