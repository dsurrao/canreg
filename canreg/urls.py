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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^patients/$', views.IndexView.as_view()),
    url(r'^patients/(?P<pk>[0-9]+)/$', views.DetailView.as_view()),
    url(r'^prelim_qns/(?P<patient_id>[0-9]+)/$', views.prelim_qns),
    url(r'^stage_cancer/(?P<patient_id>[0-9]+)/$', views.stage_cancer, name='stage_cancer'),
    url(r'^receptors/(?P<patient_id>[0-9]+)/$', views.receptors),
    url(r'^imaging_studies/(?P<patient_id>[0-9]+)/$', views.imaging_studies),
    url(r'^curative/(?P<patient_id>[0-9]+)/$', views.curative),
    url(r'^palliative/(?P<patient_id>[0-9]+)/$', views.palliative),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
