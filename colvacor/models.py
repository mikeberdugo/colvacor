from django.db import models
from django.utils.text import slugify


class Alarmas(models.Model):
    Event_ID = models.CharField(max_length=250)
    Severity = models.CharField(max_length=250)
    Event_Time = models.CharField(max_length=250)
    Node_Name = models.CharField(max_length=250)
    Event_Message = models.CharField(max_length=3000)
    Filtro = models.CharField(max_length=255)
    class Meta:
        app_label = 'colvacor'
        db_table = 'alarmas'


class ColaCreacion(models.Model):
    id_alarma = models.IntegerField()
    inc = models.CharField(max_length=240, blank=True, null=True)
    equipo = models.CharField(max_length=240)
    tipo_equipo = models.CharField(max_length=240)
    tipo_alarma = models.CharField(max_length=240)
    hora = models.CharField(max_length=240)
    central = models.CharField(max_length=240)
    gestion = models.CharField(max_length=240)
    clientes = models.CharField(max_length=240)
    tipo_evento = models.CharField(max_length=240)
    usuario = models.CharField(max_length=240)
    actividades = models.CharField(max_length=240, blank=True, null=True)
    tipo_escalamiento = models.CharField(max_length=240)
    inc_contingencia = models.CharField(max_length=240)
    hora_inicio = models.CharField(max_length=240)
    hora_ult_act = models.CharField(max_length=240, blank=True, null=True)
    estado = models.CharField(max_length=240, blank=True, null=True)
    docu1 = models.CharField(max_length=240)
    docu2 = models.CharField(max_length=240)
    docu3 = models.CharField(max_length=240)
    docu4 = models.CharField(max_length=244, blank=True, null=True)
    recuperada = models.CharField(max_length=240)
    
    class Meta:
        app_label = 'colvacor'
        db_table = 'cola_creacion'


class Descartadas(models.Model):
    id_alarma = models.IntegerField()
    equipo = models.CharField(max_length=244)
    tipo_alarma = models.CharField(max_length=244)
    hora_inicio = models.DateTimeField()
    central = models.CharField(max_length=242)
    clientes = models.CharField(max_length=244)
    usuario = models.CharField(max_length=244)
    motivo_descarte = models.CharField(max_length=244)
    hora_descarte = models.CharField(max_length=250)

    class Meta:
        app_label = 'colvacor'
        db_table = 'descartadas'


class Equipos(models.Model):
    nemonico = models.CharField(max_length=12, blank=True, null=True)
    central = models.CharField(max_length=11, blank=True, null=True)
    clientes = models.IntegerField(blank=True, null=True)
    tipo_equipo = models.CharField(max_length=240)

    class Meta:
        app_label = 'colvacor'
        db_table = 'equipos'


# CREATE TABLE `reportes` (
#   `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
#   `id_alarma` int(11) NOT NULL,
#   `inc` varchar(244) NOT NULL,
#   `equipo` varchar(244) NOT NULL,
#   `tipo_alarma` varchar(244) NOT NULL,
#   `central` varchar(244) NOT NULL,
#   `gestion` varchar(30) NOT NULL,
#   `clientes` varchar(244) NOT NULL,
#   `tipo_evento` varchar(30) NOT NULL,
#   `usuario` varchar(244) NOT NULL,
#   `tipo_escalamiento` varchar(244) NOT NULL,
#   `hora_inicio` varchar(244) NOT NULL,
#   `estado` varchar(20) NOT NULL,
#   `docu1` varchar(244) NOT NULL,
#   `docu2` varchar(250) NOT NULL,
#   `docu3` varchar(250) NOT NULL,
#   `docu4` varchar(250) NOT NULL,
#   `grupo_asignado` varchar(244) NOT NULL,
#   `cliente` varchar(250) NOT NULL,
#   `solucion` varchar(250) NOT NULL,
#   `usuario_asignado` varchar(250) NOT NULL,
#   `servicio_afectado` varchar(250) NOT NULL,
#   `ciudad` varchar(250) NOT NULL,
#   `categoria` varchar(250) NOT NULL,
#   `tecnologia` varchar(250) NOT NULL,
#   `estado_afectacion` varchar(250) NOT NULL,
#   `estado_incidencia` varchar(250) NOT NULL,
#   `fecha_fin_afectacion` varchar(250) NOT NULL,
#   `fecha_cierre` varchar(250) NOT NULL,
#   `descripcion_incidencia` varchar(250) NOT NULL,
#   `causa_raiz_2` varchar(250) NOT NULL,
#   `causa_raiz_4` varchar(250) NOT NULL,
#   `cod_cierre` varchar(250) NOT NULL,
#   `cat_niv_1` varchar(244) NOT NULL,
#   `cat_niv_2` varchar(244) NOT NULL,
#   `cat_niv_3` varchar(244) NOT NULL,
#   `hora` timestamp(6) NOT NULL DEFAULT current_timestamp(6),
#   `hora_ult_act` timestamp(6) NOT NULL DEFAULT current_timestamp(6),
#   `hora_asignacion` varchar(250) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



class Reportes(models.Model):
    id_alarma = models.IntegerField()
    inc = models.CharField(max_length=244)
    equipo = models.CharField(max_length=244)
    tipo_alarma = models.CharField(max_length=244)
    central = models.CharField(max_length=244)
    gestion = models.CharField(max_length=30)
    clientes = models.CharField(max_length=244)
    tipo_evento = models.CharField(max_length=30)
    usuario = models.CharField(max_length=244)
    tipo_escalamiento = models.CharField(max_length=244)
    hora_inicio = models.CharField(max_length=244)
    estado = models.CharField(max_length=20)
    docu1 = models.CharField(max_length=244)
    docu2 = models.CharField(max_length=250)
    docu3 = models.CharField(max_length=250)
    docu4 = models.CharField(max_length=250)
    grupo_asignado = models.CharField(max_length=250)
    cliente = models.CharField(max_length=250)
    solucion = models.CharField(max_length=250)
    usuario_asignado = models.CharField(max_length=250)
    servicio_afectado = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    categoria = models.CharField(max_length=250)
    estado_afectacion = models.CharField(max_length=250)
    estado_incidencia = models.CharField(max_length=250)
    fecha_fin_afectacion = models.CharField(max_length=250)
    fecha_cierre = models.CharField(max_length=250)
    causa_raiz_2 = models.CharField(max_length=250)
    causa_raiz_4 = models.CharField(max_length=250)
    cod_cierre = models.CharField(max_length=250)
    cat_niv_1 = models.CharField(max_length=250)
    cat_niv_2 = models.CharField(max_length=250)
    cat_niv_3 = models.CharField(max_length=250)
    hora  = models.CharField(max_length=250)
    hora_ult_act = models.CharField(max_length=250)
    hora_asignacion = models.CharField(max_length=250)
    tecnologia = models.CharField(max_length=250)
    descripcion_incidencia = models.CharField(max_length=250)
    notificado = models.CharField(max_length=250)

    class Meta:
        app_label = 'colvacor'
        db_table = 'reportes'


class Usuarios(models.Model):
    nombre = models.CharField(max_length=244)
    cargo = models.CharField(max_length=244)
    gestion = models.CharField(max_length=244)
    segmento = models.CharField(max_length=244)
    correo = models.CharField(max_length=244)
    username = models.CharField(max_length=244)
    clave = models.CharField(max_length=244)
    tipo_usuario = models.CharField(max_length=44)
    cod_etb = models.CharField(max_length=20)
    imagen_usuario = models.CharField(max_length=255)
    numero_telefono = models.CharField(max_length=10)
    token = models.CharField(max_length=12)
    
    class Meta:
        app_label = 'colvacor'
        db_table = 'usuarios'
        

class Correos(models.Model):
    gestion = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    class Meta:
        app_label = 'colvacor'
        db_table = 'correos'

