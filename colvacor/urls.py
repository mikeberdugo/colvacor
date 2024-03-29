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
from colvacor.views.todos import *
from colvacor.views.operators.operadores import * 
from colvacor.views.automa.auto import * 
from colvacor.views.analitic.analitic import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name = 'inicio'),
    path('sistema1/',sistema1,name = 'sistema1'),
    path('gestion/<int:alarma_id>',gestion,name='gestion'),
    path('prueba/',prueba),
    path('usuarios/',usuarios,name = 'usuarios'),
    path('usuarios/nuevo-usuario/',nuevo,name = 'nuevo'),
    path('usuarios/modifciar/<int:user_id>/',modifica_usuario, name = 'modificar'),
    path('usuarios/eliminar-usuario/<int:user_id>/',eliminar_usuario, name='eliminar-usuario'),
    path('alarmas/',alarmas,name = 'alarmas'),
    path('alarmas/descartada/<int:descartada_id>/',alarmas_descartadas, name='descartada'),
    path('casos/',casos,name = 'casos'),
    path('casos/caso/<int:reporte_id>/',caso,name = 'caso'),
    path('reportes/',reportes,name = 'reportes'),
    path('descartadas/',descartadas,name = 'descartadas'),
    path('user/',user,name = 'user'),
    path('cambio/', cambio_numero, name='cambio_numero'),
    path('imagen/', imagen, name='imagen'),
    path('correos/',correos,name = 'correos'),
    path('correos/nuevos/',nuevo_correo,name = 'nuevocorreo'),
    path('correos/eliminar/<int:mail_id>/',eliminar_correo,name = 'eliminarcorreo'),
    path('cerrar/',cerrar,name = 'cerrar'),
    path('cola/',cola,name = 'cola'),
    path('cola/generar/<int:cola_id>/',creacion_stela,name = 'stela'),
    path('cola/actualzar/',actualiza_stela,name = 'actualiza_stela'),
    path('cola/actualzar/reporte/<int:reporte_id>',guarda_stela,name = 'guarda_stela'),
    path('incidente/<int:alarma_id>',incidente,name = 'incidente'),
    path('carga/', carga_stela, name='carga'), 
    path('ver_mensaje/mensaje_stela/<int:mensaje_id>', mensaje_stela, name='mensaje_stela'),
    path('ver_mensaje/', ver_mensaje, name='ver_mensaje'),
    path('alarma2/', alarmas_view, name='alarmas2'),
    path('resta/', resta, name='reestablecer'),
    path('password/<str:user_token>',cambio_password),
    # operadores  

    path('operadores/core',operators_core,name='core'),
    path('operadores/nodo',operators_nodo,name='nodo'),
    path('operadores/gpon',operators_gpon,name='gpon'),
    path('operadores/nal',operators_nal,name='nal'),
    path('operadores/adsl',operators_adsl,name='adsl'),
    path('operadores/local',operators_local,name='local'),
    path('operadores/iptv',operators_iptv,name='iptv'),
    path('operadores/mpls',operators_mpls,name='mpls'),

    #analitic 
    path('prueba/analitica',mpls_analysis,name='analitica-1'),

    # Esta línea captura cualquier ruta no definida y la dirige a la vista personalizada
    path('<str:ruta_no_definida>/', pagina_no_encontrada, name='pagina_no_encontrada'),
]
