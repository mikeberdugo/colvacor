from django.shortcuts import render, redirect ,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from colvacor.models import Alarmas,Usuarios,ColaCreacion
from django.contrib.auth.hashers import make_password, check_password
#### loging 

### prueba de alarmas 

def alarmas_view(request):
    alarma = Alarmas.objects.all()
    return render(request, 'prueba.html', {'alarma': alarma})
#### prueba correo 


def enviar_correo(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('recipient_email')]

        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'correo_enviado.html')

    return render(request, 'formulario_correo.html')


def inicio(request):
    error_message = []
    aux = True 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = Usuarios.objects.all()
        for user in users :             
            if user.username == username and  check_password(password, user.clave) : 
                return redirect(sistema1)
                aux = True
            else :
                aux = False
        if aux == False : 
            error_message.append( "Nombre de usuario o contraseña incorrectos.")
    return render(request,"index.html",{'error_message': error_message})


def resta(request):
    return render(request ,'reestablecer.html')

### sistema 1 y gestion de vistas 
def sistema1(request):
    
    if request.method == 'POST':
        
        show_view1 = request.POST.get('view1') == 'on'
        show_view2 = request.POST.get('view2') == 'on'
        show_view3 = request.POST.get('view3') == 'on'
        show_view4 = request.POST.get('view4') == 'on'
        show_view5 = request.POST.get('view5') == 'on'
        show_view6 = request.POST.get('view6') == 'on'
        show_view7 = request.POST.get('view7') == 'on'
        show_view8 = request.POST.get('view8') == 'on'
        
        context = {
            'show_view1': show_view1,
            'show_view2': show_view2,
            'show_view3': show_view3,
            'show_view4': show_view4,
            'show_view5': show_view5,
            'show_view6': show_view6,
            'show_view7': show_view7,
            'show_view8': show_view8,
        }
    else:
        context = {
            'show_view1': True,
            'show_view2': True,
            'show_view3': True,
            'show_view4': True,
            'show_view5': True,
            'show_view6': True,
            'show_view7': True,
            'show_view8': True,

        }
    return render(request,"sistema1.html" , context)


def sistema2(request):
    
    if request.method == 'POST':
        
        show_view1 = request.POST.get('view1') == 'on'
        show_view2 = request.POST.get('view2') == 'on'
        show_view3 = request.POST.get('view3') == 'on'
        show_view4 = request.POST.get('view4') == 'on'
        show_view5 = request.POST.get('view5') == 'on'
        show_view6 = request.POST.get('view6') == 'on'
        show_view7 = request.POST.get('view7') == 'on'
        show_view8 = request.POST.get('view8') == 'on'
        
        context = {
            'show_view1': show_view1,
            'show_view2': show_view2,
            'show_view3': show_view3,
            'show_view4': show_view4,
            'show_view5': show_view5,
            'show_view6': show_view6,
            'show_view7': show_view7,
            'show_view8': show_view8,
        }
    else:
        context = {
            'show_view1': True,
            'show_view2': True,
            'show_view3': True,
            'show_view4': True,
            'show_view5': True,
            'show_view6': True,
            'show_view7': True,
            'show_view8': True,

        }
    return render(request,"sistema1.html" , context)



#### plantilla --- prueba 
def prueba(request):    
    return render(request,"plantilla.html")


#### plantilla ---  gestion de usuario 
def usuarios(request): 
    users = Usuarios.objects.all()    
    return render(request,"./admin/admin_usuarios.html",{'users': users})

def eliminar_usuario(request, user_id):
    user = get_object_or_404(Usuarios, id=user_id)
    user.delete()
    return redirect(usuarios)

def modifica_usuario(request, user_id):
    
    user = Usuarios.objects.get(pk=user_id)
    if request.method == 'POST':
        user.nombre = request.POST['nombre']
        user.cargo = request.POST['cargo']
        user.gestion = request.POST['gestion']
        user.segmento = request.POST['segmento']
        user.correo = request.POST['correo']
        user.username = request.POST['username']
        user.tipo_usuario = request.POST['tipo_usuario']
        user.cod_etb = request.POST['cod_etb']
        user.save()  # Guarda los cambios en la base de datos
        return redirect(usuarios)
    return render(request,"./admin/modificar.html",{'user': user})

#### plantilla --- nuevo 
def nuevo(request): 
    if request.method == 'POST':
        name = request.POST['name']
        cargo = request.POST['cargo']
        segmento = request.POST['segmento']
        gestion = request.POST['gestion']
        correo = request.POST['correo']
        user = request.POST['user']
        clave = request.POST['clave']
        hashed_password = make_password(clave)        
        nuevo_usuario = Usuarios(nombre=name,cargo =cargo,gestion = gestion,segmento=segmento , correo = correo , username = user,tipo_usuario = '1' ,cod_etb = '2020B',clave = hashed_password  )
        nuevo_usuario.save()
        
    else : 
        print('no llego nada')
    # nuevo_producto = Producto(nombre=nombre, precio=precio)
    # nuevo_producto.save()
    return render(request,"./admin/nuevo_usuario.html")

#### plantilla --- alarmas descartadas 
def alarmas(request):  
    alarma = Alarmas.objects.all()
    return render(request,"./admin/alarma.html",{'alarma': alarma})


#### plantilla --- casos reportados  
def casos(request):    
    return render(request,"./admin/casos.html")


#### plantilla --- generar un reporte  
def reportes(request):    
    return render(request,"./admin/generar.html")


#### plantilla --- user 
def user(request):    
    return render(request,"./admin/vista_usuario.html")

#### plantilla --- out 
def cerrar(request):
    return render(request,"./admin/cerrar.html")

### las colas de estela y el almacenamiento nuevo 


def cola(request):   
    colas = ColaCreacion.objects.all()
    
    return render(request,"./admin/cola_stela.html",{'colas': colas})

def stela(request,cola_id):
    cola = ColaCreacion.objects.get(pk=cola_id) 
    
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
    return render(request,"./admin/ver_stela.html",{'mensaje': mensaje, 'cola': cola})
