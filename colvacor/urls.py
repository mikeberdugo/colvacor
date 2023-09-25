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
from colvacor.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name = 'inicio'),
    path('sistema1/',sistema1,name = 'sistema1'),
    path('gestion/<int:alarma_id>',gestion,name='gestion'),
    path('prueba/',prueba),
    path('usuarios/',usuarios,name = 'usuarios'),
    path('nuevo-usuario/',nuevo,name = 'nuevo'),
    path('alarmas/',alarmas,name = 'alarmas'),
    path('alarma-descartada/<int:descartada_id>/',alarmas_descartadas, name='descartada'),
    path('casos/',casos,name = 'casos'),
    path('caso/<int:reporte_id>/',caso,name = 'caso'),
    path('reportes/',reportes,name = 'reportes'),
    path('user/',user,name = 'user'),
    path('cambio/', cambio_numero, name='cambio_numero'),
    path('imagen/', imagen, name='imagen'),
    path('correos/',correos,name = 'correos'),
    path('correos/nuevos/',nuevo_correo,name = 'nuevocorreo'),
    path('correos/eliminar/<int:mail_id>/',eliminar_correo,name = 'eliminarcorreo'),
    path('cerrar/',cerrar,name = 'cerrar'),
    path('cola/',cola,name = 'cola'),
    path('incidente/<int:alarma_id>',incidente,name = 'incidente'),
    path('stela/<int:cola_id>/',stela,name = 'stela'),
    path('alarma2/', alarmas_view, name='alarmas2'),
    path('resta/', resta, name='reestablecer'),
    path('mail/', enviar_correo),
    path('modifciar/<int:user_id>/',modifica_usuario, name = 'modificar'),
    path('eliminar-usuario/<int:user_id>/',eliminar_usuario, name='eliminar-usuario')
]
