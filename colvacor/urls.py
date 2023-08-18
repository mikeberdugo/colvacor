"""colvacor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from colvacor.views import inicio,sistema1,sistema2,prueba,usuarios,nuevo,user,reportes,alarmas,casos,cerrar,stela


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('sistema1/',sistema1,name = 'sistema1'),
    path('sistema2/',sistema2,name = 'sistema2'),
    path('prueba/',prueba),
    path('usuarios/',usuarios,name = 'usuarios'),
    path('nuevo-usuario/',nuevo,name = 'nuevo'),
    path('alarmas/',alarmas,name = 'alarmas'),
    path('casos/',casos,name = 'casos'),
    path('reportes/',reportes,name = 'reportes'),
    path('user/',user,name = 'user'),
    path('cerrar/',cerrar,name = 'cerrar'),
    path('stela/',stela,name = 'stela'),
]
