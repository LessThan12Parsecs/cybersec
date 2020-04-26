"""cybersecweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('list.urls')),
    path('s3/', include('s3.urls')),
    path('ec2/', include('ec2.urls')),
    path('orgs/', include('orgs.urls')),
    path('rds/', include('rds.urls')),
    path('iam/', include('iam.urls')),
    path('lambdas/', include('lambdas.urls')),
    path('', RedirectView.as_view(url='list/', permanent=True)),
    path('tag/', include('tag.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)