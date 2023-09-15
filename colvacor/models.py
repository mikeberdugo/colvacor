from django.db import models


class Alarmas(models.Model):
    equipo = models.CharField(max_length=245)
    tipo_alarma = models.CharField(max_length=245)
    hora_inicio = models.DateTimeField()
    central = models.CharField(max_length=244)
    clientes = models.CharField(max_length=244)

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


class Reportes(models.Model):
    id_alarma = models.IntegerField()
    inc = models.CharField(max_length=244)
    equipo = models.CharField(max_length=244)
    tipo_alarma = models.CharField(max_length=244)
    hora = models.DateTimeField()
    central = models.CharField(max_length=244)
    gestion = models.CharField(max_length=30)
    clientes = models.CharField(max_length=244)
    tipo_evento = models.CharField(max_length=30)
    usuario = models.CharField(max_length=244)
    tipo_escalamiento = models.CharField(max_length=244)
    hora_inicio = models.CharField(max_length=244)
    hora_ult_act = models.DateTimeField()
    estado = models.CharField(max_length=20)
    docu1 = models.CharField(max_length=244)
    docu2 = models.CharField(max_length=250)
    docu3 = models.CharField(max_length=250)
    docu4 = models.CharField(max_length=250)
    grupo_asignado = models.CharField(max_length=250)
    cat_niv_1 = models.CharField(max_length=250)
    cat_niv_2 = models.CharField(max_length=250)
    cat_niv_3 = models.CharField(max_length=250)
    hora  = models.DateTimeField()
    hora_asignacion = models.CharField(max_length=250)
    



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
    
    class Meta:
        app_label = 'colvacor'
        db_table = 'usuarios'
