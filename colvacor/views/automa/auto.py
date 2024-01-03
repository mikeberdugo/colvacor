from django.shortcuts import render, redirect ,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from colvacor.models import *
from django.template.loader import render_to_string

### imagen 
from django.conf import settings
import pandas as pd

## carga datos a la base de datos 
def carga_stela(request):
    
    if request.method == 'POST':
        archivo_excel = request.FILES['archivo']
        if archivo_excel.name.endswith('.xls') or archivo_excel.name.endswith('.xlsx'):
            df = pd.read_excel(archivo_excel)
            for index, row in df.iterrows():
                Event_ID = row['Event ID']
                Severity = row['Severity']
                Event_Time = row['Event Time']
                Node_Name = row['Node Name']
                Event_Message = row['Event Message']
                Filtro = row['Filtro']
                Alarmas.objects.create(Event_ID=Event_ID, Severity=Severity, Event_Time=Event_Time, Node_Name=Node_Name, Event_Message=Event_Message , Filtro=Filtro)
                
    return render(request,"./admin/carga_stella.html")

## actializa los datos en la db desde sus valores de remedi 

def actualiza_stela(request):
    reportes =  Reportes.objects.filter(cliente__isnull=True, solucion__isnull=True) | \
                        Reportes.objects.filter(cliente__exact='', solucion__exact='')
        
    # Formatea la hora como HH:MM:SS
    return render(request,"./admin/actualiza_stela.html",{ 'reportes' : reportes })

## genera el reporte 

def guarda_stela(request,reporte_id):
    reporte =  Reportes.objects.get(pk=reporte_id)
    
    mensaje = (
        f"FALLA SOBRE:{reporte.equipo}, DE CENTRAL {reporte.central}, "
        f"RED ERICSSON 180K\nHORA DE ALARMA: {reporte.hora_inicio}\nDESCRIPCIÓN DEL EVENTO: "
        f"EQUIPO ECN330 SE OBSERVA ALARMADO EN GESTIÓN Y NO RESPONDE PRUEBAS DE CONECTIVIDAD."
        f"\nRED: RED ERICSSON 180K.\nENLACE O EQUIPO AFECTADO (NEMÓNICO O SERVICIO): {reporte.equipo}"
        f"\nZONA DE EVENTO: {reporte.central}\nDIRECCIÓN: \nIP: \nCLIENTE: ADSL \nNO. CLIENTES AFECTADOS:"
        f" {reporte.clientes}\nAFECTACIÓN (TOTAL/PARCIAL): TOTAL \nSÍNTOMA: CLIENTES NO SINCRONIZAN "
        f"\nPRUEBAS REALIZADAS: EQUIPO ECN330 SE OBSERVA ALARMADO EN GESTIÓN Y NO RESPONDE PRUEBAS DE CONECTIVIDAD."
        f" INTERFAZ SOBRE LA RED METRO SE ENCUENTRA; DOWN, NO APRENDE MACS. . PERSONAL DE CODENSA   "
        f"NO REPORTA FALLAS Y/O MANTENIMIENTOS DE ENERGÍA EN EL SECTOR \nDIAGNÓSTICO: POSIBLE FALLA DE EQUIPO ECN330 "
        f"\nVOBO INGENIERO: Lizeth Vacca"
    )
    return render(request,"./admin/vista_actualiza_stela.html",{'mensaje': mensaje, 'reporte' : reporte })




def cola(request): # 
    colas = ColaCreacion.objects.filter(recuperada='NO')
    return render(request,"./admin/cola_stela.html",{'colas': colas})

def creacion_stela(request,cola_id): # 
    cola = ColaCreacion.objects.get(pk=cola_id)#caso_id
    if request.method == 'POST':
        
        id_alarma = int( request.POST['id_alarma'])
        central = request.POST['central']
        clientes1 = request.POST['clientes1']
        tipo_alarma = request.POST['tipo_alarma']
        gestion = request.POST['gestion']
        tipo_alarma = request.POST['tipo_alarma']
        resumen = request.POST['resumen']
        plantilla = request.POST['plantilla']
        tipo_evento = request.POST['tipo_evento']
        hora_inicio = request.POST['hora_inicio'] ## verificacion de este valor 
        clientes = request.POST['clientes']
        docu1 = request.POST['docu1']
        docu2 = request.POST['docu2']
        docu3 = request.POST['docu3']
        docu4 = request.POST['docu4']
        equipo = request.POST['equipo']
        usuario = request.POST['usuario']
        hora = request.POST['hora']
        Grupo_reporte = request.POST['Grupo_reporte']
        hora_reporte = request.POST['hora_reporte']
        tipo_escalamiento = request.POST['tipo_escalamiento']
        inc = request.POST['inc']
        hora_actual = 'hpra'
        reporte = Reportes(id_alarma = id_alarma , inc = inc, equipo  = equipo , tipo_alarma = tipo_alarma , central = central ,gestion = gestion , clientes = clientes, 
                    tipo_evento = tipo_evento ,usuario = usuario , tipo_escalamiento = tipo_escalamiento , hora_inicio = hora_inicio ,
                    docu1= docu1 , docu2= docu2 ,docu3= docu3 ,docu4= docu4 , grupo_asignado = Grupo_reporte , hora_asignacion =  hora_reporte , hora_ult_act =hora_actual ,
                    hora = hora , )
        reporte.save()
        user = get_object_or_404(Alarmas, id=cola.id_alarma)
        user.delete()
        cola.recuperada = 'SI'
        cola.save()
        subject = 'Creacion Incidencia '+str(cola.inc) +  ' - Impacto alto ADSL'
        message = ''
        from_email = settings.EMAIL_HOST_USER
        
        html_message =  render_to_string('formulario_correo.html',{'cola':reporte})
        
        #'noc_etb_adsl_eda@etb.com.co','francoby.perezg@gmail.com',
        recipient_list = ['manuel.david.13.b@gmail.com']
        send_mail(subject, message, from_email, recipient_list,fail_silently=False,html_message=html_message)
        return redirect('cola')
    
        #nuevo_usuario = Usuarios(nombre=name,cargo =cargo,gestion = gestion,segmento=segmento , correo = correo , username = user,tipo_usuario = '1' ,cod_etb = '2020B',clave = hashed_password  )
        #nuevo_usuario.save()

    #Reportes
    mensaje = (
        f"FALLA SOBRE: {cola.tipo_equipo} {cola.equipo}, DE CENTRAL {cola.central}, "
        f"RED ERICSSON 180K\nHORA DE ALARMA: {cola.hora_inicio}\nDESCRIPCIÓN DEL EVENTO: "
        f"EQUIPO ECN330 SE OBSERVA ALARMADO EN GESTIÓN Y NO RESPONDE PRUEBAS DE CONECTIVIDAD."
        f"\nRED: RED ERICSSON 180K.\nENLACE O EQUIPO AFECTADO (NEMÓNICO O SERVICIO): {cola.equipo}"
        f"\nZONA DE EVENTO: {cola.central}\nDIRECCIÓN: \nIP: \nCLIENTE: ADSL \nNO. CLIENTES AFECTADOS:"
        f" {cola.clientes}\nAFECTACIÓN (TOTAL/PARCIAL): TOTAL \nSÍNTOMA: CLIENTES NO SINCRONIZAN "
        f"\nPRUEBAS REALIZADAS: EQUIPO ECN330 SE OBSERVA ALARMADO EN GESTIÓN Y NO RESPONDE PRUEBAS DE CONECTIVIDAD."
        f" INTERFAZ SOBRE LA RED METRO SE ENCUENTRA; DOWN, NO APRENDE MACS. . PERSONAL DE CODENSA   "
        f"NO REPORTA FALLAS Y/O MANTENIMIENTOS DE ENERGÍA EN EL SECTOR \nDIAGNÓSTICO: POSIBLE FALLA DE EQUIPO ECN330 "
        f"\nVOBO INGENIERO: Lizeth Vacca"
    )
    
# Se ha creado el caso {inc} con impacto Alto del equipo
# Incidente:{inc}
# Clientes afectados:{clientes}
# Hora de Inicio afectación:{hora_inicio}
# Gestión que reporta el INC:{gestion}
# Grupo Asignado:{grupo_asignado}
# Esta es una notificación automática de Colvacor Intellisense
    

    return render(request,"./admin/ver_stela.html",{'mensaje': mensaje, 'cola': cola})





def ver_mensaje(request):
    reportes = Reportes.objects.filter(notificado__exact='NO')
    return render(request,"./admin/ver_mensaje.html",{'reportes':reportes})



def mensaje_stela(request,mensaje_id):
    report = Reportes.objects.get(pk=mensaje_id)
    report.notificado = 'SI'
    report.save()
    return redirect('ver_mensaje')




