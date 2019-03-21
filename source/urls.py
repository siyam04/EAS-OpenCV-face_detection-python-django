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
from rest_framework import routers
# from django.conf.urls import url, include
from django.conf.urls.static import static

# App views
from user_authentication.views import Users


# Router DRF
router = routers.DefaultRouter()
# router.register(r'matched-user', Users, basename='matched-user')


urlpatterns = [

    # System dashboard path
    path('admin/', admin.site.urls),

    # user_authentication app's path
    path('user/', include('user_authentication.urls')),

    # API path
    path('api-auth/', include('rest_framework.urls')),

    # Router path
    path('matched-user/<username>', Users.as_view())


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Debugging toolbar integration
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [

        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

