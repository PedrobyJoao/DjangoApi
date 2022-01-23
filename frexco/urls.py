"""frexco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from api.views import RegionViewSet, FruitViewSet
from rest_framework import routers
from api import views


router_R = routers.DefaultRouter()
router_R.register(r'Region', RegionViewSet)

router_F = routers.DefaultRouter()
router_F.register(r'Fruit', FruitViewSet)


urlpatterns = [
    path('', views.apiOverview, name="API Overview"),
    path('', include(router_F.urls)),
    path('', include(router_R.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
