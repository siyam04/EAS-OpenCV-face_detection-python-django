"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# App views
from user_authentication.api.views import Users


# Project source paths
urlpatterns = [

    # System dashboard path
    path('admin/', admin.site.urls),

    # API
    path('matched-user/<username>/', Users.as_view()),

    # DRF
    path('api-auth/', include('rest_framework.urls')),

    # user_authentication app's path
    path('user/', include('user_authentication.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Debugging toolbar integration for browser
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [

        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

