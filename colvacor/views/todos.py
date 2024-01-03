from django.shortcuts import render, redirect ,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from colvacor.models import *
from django.contrib.auth.hashers import make_password, check_password

from django.template.loader import render_to_string



### imagen 
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import uuid
from django.db.models import Q

### modulos personales
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout,authenticate
#### loging
import random
import string


def texto_aleatorio(max_length):
    caracteres = string.ascii_letters + string.digits
    longitud = random.randint(1, max_length)
    texto = ''.join(random.choice(caracteres) for _ in range(longitud))
    return texto
### prueba de alarmas

def alarmas_view(request):
    context = request.session.get('context', {})
    alarma = Alarmas.objects.all()
    return render(request, 'prueba.html', {'context' :context,'alarma': alarma})
#### prueba correo


# def enviar_correo(request):
#     if request.method == 'POST':
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = ['mdberdugo@personalsoft.com','manuel.david.13.b@gmail.com']

#         send_mail(subject, message, from_email, recipient_list)
#         #return render(request, 'correo_enviado.html')
#     return render(request, 'formulario_correo.html')


def inicio(request):
    error_message = []
    views = {}
    context = request.session.get('context', {})
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user2 = authenticate(username=username, password=password)
        try:
            user = Usuarios.objects.get(username=username)            
            if user is not None :
                if check_password(password, user.clave):  # Verifica la contraseña encriptada
                    #login(request, user)
                    for i in range(1, 9):
                        view_key = f'show_view{i}'
                        views[view_key] = True
                    nombre_completo = user.nombre
                    nombres = nombre_completo.split(" ")
                    views['user_id'] = user.id
                    views['primer_nombre'] = nombres[0]
                    views['ultimo_nombre'] = nombres[2]
                    views['gestion'] = user.gestion
                    views['cargo'] = user.cargo
                    context = views  # Usa el diccionario como contexto
                    request.session['context'] = context                    
                    return redirect('sistema1')
                else:
                    error_message.append("contraseña incorrecta.")
        except Exception as e:
    # Captura la excepción y la almacena en la variable 'e'
            print(f"Se produjo un error: {str(e)}")  # Imprime el mensaje de error 
            error_message.append( "Nombre de usuario incorrecto" )
    return render(request, "index.html", {'error_message': error_message})

def resta(request):
    error_message = []
    if request.method == 'POST':
        correo = str(request.POST['correo'])
        try:        
            user = Usuarios.objects.get(correo=correo)
            if user is not None :
                subject = 'Correo de Validacion Usuario Colvacor '
                message = 'prueba de correo : http://127.0.0.1:3000/password/'+user.token
                from_email = settings.EMAIL_HOST_USER
                #html_message =  render_to_string('formulario_correo.html',{'cola':reporte}) html_message=html_message
                #'noc_etb_adsl_eda@etb.com.co','francoby.perezg@gmail.com',
                recipient_list = [correo,'manuel.david.13.b@gmail.com']
                send_mail(subject, message, from_email, recipient_list)
                return redirect('inicio')
        except : 
            error_message.append( "El Correo Ingresado es Incorrecto" )
        
    return render(request ,'reestablecer.html',{'error_message': error_message})


def cambio_password(request,user_token):
    error_message = []
    user = Usuarios.objects.get(token=user_token)  
    if request.method == 'POST':
        password1 = str(request.POST['password1'])
        password2 = str(request.POST['password2'])
        #http://127.0.0.1:3000/1234
        
        if password1 == password2 :
            hashed_password = make_password(password1)
            user.clave = hashed_password 
            user.save()
            return redirect('inicio')           
        else : 
            error_message.append( "las contraseñas ingresadas no son iguales " )
            
    return render(request,'cambio.html',{'error_message': error_message})


### sistema 1 y gestion de vistas
def sistema1(request):    
    context = request.session.get('context', {})    
    # Define un diccionario con las claves y sus valores iniciales
    views = {}
    if request.method == 'POST':
        # Recorre las vistas de 1 a 8 y actualiza el diccionario
        for i in range(1, 9):
            view_key = f'show_view{i}'
            context[view_key] = request.POST.get(f'view{i}') == 'on'
    
    context['desc'] = Descartadas.objects.count()
    context['caso'] = Reportes.objects.count()
    context['cola'] = ColaCreacion.objects.filter(recuperada='NO').count()
    #context = views  # Usa el diccionario como contexto
    request.session['context'] = context
    
    alarmas = Alarmas.objects.all()
    DesempenoMPLS = Alarmas.objects.filter(Filtro='Filtro: Desempeño MPLS') 
    LSPs_Status = Alarmas.objects.filter(Filtro='Filtro: LSPs y LDPs Status') 
    Subscribers = Alarmas.objects.filter(Filtro='Filtro: Subscribers') 
    Trafico_Interfaces = Alarmas.objects.filter(Filtro='Filtro: TraficoInterfaces') 
    Falla_componentes = Alarmas.objects.filter(Filtro='Filtro: FallaCompMPLS') 
    CGNAt = Alarmas.objects.filter(Filtro='mams') 
    BGP_Rr = Alarmas.objects.filter(Filtro='BGP peer 10.32.0.13') 
    Potencia_Interfaces =  Alarmas.objects.filter(Filtro='uei.opennms.org/translator/ETB/RxPowerInterface') 
    Troncales = Alarmas.objects.filter(Filtro='link') 
    
    colaCreacion = ColaCreacion.objects.filter(recuperada='NO')
    
    return render(request, "sistema1.html", {
        'context' :context ,
        'alarmas' : alarmas, 
        'colaCreacion': colaCreacion ,
        'DesempenoMPLS':DesempenoMPLS,
        'LSPs_Status':LSPs_Status,
        'Subscribers':Subscribers,
        'Trafico_Interfaces':Trafico_Interfaces,
        'Falla_componentes':Falla_componentes,
        'CGNAT':CGNAt,
        'BGP_RR':BGP_Rr,
        'Potencia_Interfaces':Potencia_Interfaces,
        'Troncales':Troncales        
        })



def gestion(request,alarma_id):
    context = request.session.get('context', {}) # 'context' :context ,
    alarma = Alarmas.objects.get(pk=alarma_id)
    try:
        equipo = Equipos.objects.get(nemonico=alarma.Node_Name)
    except Equipos.DoesNotExist:
        equipo = {'central':'ERROR - Equipo no encontrado - comuniquese con gestion ', 'clientes':'ERROR - Equipo no encontrado - comuniquese con gestion '}

    return render(request,"./admin/gestionar.html",{'context' :context ,'alarma': alarma , 'equipo' :equipo})

def incidente(request,alarma_id):
    alarma = Alarmas.objects.get(pk=alarma_id)
    #docu3
    inciden = ColaCreacion(id_alarma = alarma.id , inc ='' , tipo_alarma = alarma.tipo_alarma , hora_inicio = alarma.hora_inicio , 
                    central = alarma.central,clientes = alarma.clientes)
    inciden.save()
    return redirect('sistema1')
    
#### plantilla --- prueba
def prueba(request):
        # Agrega un mensaje de éxito a la lista de mensajes
    messages_list = [
        {'tag': 'success', 'text': "Dato 1 guardado correctamente."},
        {'tag': 'error', 'text': "Error al guardar Dato 2."},
        {'tag': 'warning', 'text': "Dato 3 guardado correctamente."},

        # Puedes agregar más mensajes según sea necesario
    ]

    return render(request,"prueba.html",{'messages_list': messages_list})

def descartadas(request):
    return render(request,"prueba.html")


#### plantilla ---  gestion de usuario
def usuarios(request):
    context = request.session.get('context', {})
    users = Usuarios.objects.all()
    return render(request,"./admin/admin_usuarios.html",{'context' :context,'users': users})

def eliminar_usuario(request, user_id):
    user = get_object_or_404(Usuarios, id=user_id)
    user.delete()
    return redirect(usuarios)

def modifica_usuario(request, user_id):
    context = request.session.get('context', {})#'context' :context,
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
    return render(request,"./admin/modificar.html",{'context' :context,'user': user})

#### plantilla --- nuevo
def nuevo(request):
    context = request.session.get('context', {})#'context' :context,
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
        return redirect(usuarios)
    # nuevo_producto = Producto(nombre=nombre, precio=precio)
    # nuevo_producto.save()
    return render(request,"./admin/nuevo_usuario.html",{'context' :context})


def correos(request):    
    context = request.session.get('context', {})
    core =  Correos.objects.filter(gestion='CORE') 
    node =  Correos.objects.filter(gestion='NODO') 
    gpon =  Correos.objects.filter(gestion='GPON') 
    txnal = Correos.objects.filter(gestion='TX NAL')
    adsl =  Correos.objects.filter(gestion='ADSL') 
    txlocal = Correos.objects.filter(gestion='TX LOCAL')
    iptv = Correos.objects.filter(gestion='IPTV')
    mpls = Correos.objects.filter(gestion='MPLS')
    
    return render(request,"./admin/correos.html",{'context' :context,'core':core,'node':node , 'gpon':gpon ,'txnal' : txnal ,'adsl':adsl, 'txlocal':txlocal , 'iptv':iptv , 'mpls':mpls})


def nuevo_correo(request):
    context = request.session.get('context', {})#'context' :context,
    if request.method == 'POST':
        gestion = request.POST['gestion']
        correo = request.POST['correo']
        nuevoCorreo =  Correos(gestion = gestion , correo = correo )
        nuevoCorreo.save()
        return redirect(correos)
        
    return render(request,"./admin/nuevocorreo.html",{'context' :context})


def eliminar_correo(mail_id):
    correo = get_object_or_404(Correos, id=mail_id)
    correo.delete()
    return redirect(correos)

#### plantilla --- alarmas descartadas
def alarmas(request):
    context = request.session.get('context', {})#'context' :context,
    descartadas = Descartadas.objects.all()
    return render(request,"./admin/alarma.html",{'context' :context,'descartadas': descartadas})


def alarmas_descartadas(request,descartada_id):
    context = request.session.get('context', {})#'context' :context,
    descartada = Descartadas.objects.get(pk=descartada_id)
    return render(request,"./admin/descartada.html",{'context' :context,'descartada': descartada})

#### plantilla --- casos reportados
def casos(request):
    context = request.session.get('context', {}) # 'context' :context ,
    reportes = Reportes.objects.all()
    return render(request,"./admin/casos.html",{'context' :context ,'reportes': reportes})

def caso(request,reporte_id):
    context = request.session.get('context', {}) # 'context' :context ,
    reporte = Reportes.objects.get(pk=reporte_id)#caso_id
    return render(request,"./admin/ver_creados.html",{'context' :context ,'reporte': reporte})


#### plantilla --- generar un reporte
def reportes(request):
    context = request.session.get('context', {}) # 'context' :context ,
    return render(request,"./admin/generar.html",{'context' :context})


#### plantilla --- user
def user(request):
    context = request.session.get('context', {})#'context' :context,
    user_id = context['user_id']  
    user = Usuarios.objects.get(pk=user_id)
    return render(request,"./admin/vista_usuario.html",{'context' :context,'user':user})

def cambio_numero(request):
    if request.method == 'POST':
        nnu = request.POST['nuevo_numero']
        user_id = request.POST['user_id']
        user = Usuarios.objects.get(pk=user_id)
        user.numero_telefono = nnu
        user.save()
        return redirect('user')
    
def imagen(request):
    if request.method == 'POST' :    
        imagen = request.FILES.get('imagen')
        if imagen:
            user_id = request.POST['user_id']
            user = Usuarios.objects.get(pk=user_id)
            nombre_archivo = texto_aleatorio(12)
            name = nombre_archivo + '.jpg'
            user.imagen_usuario = nombre_archivo
            user.save()
            ruta_destino = f'{settings.MEDIA_ROOT}{name}'
            #print(settings.)
            with open(ruta_destino, 'wb') as archivo_destino:
                for chunk in imagen.chunks():
                    archivo_destino.write(chunk)
            # Guarda la imagen en la ubicación especificada
            return redirect('user')
        

#### plantilla --- out
def cerrar(request):
    context = request.session.get('context', {})#'context' :context,
    context.clear()
    print(context)
    request.session['context'] = context   
    print(request.session['context'])
    return redirect('inicio')

### las colas de estela y el almacenamiento nuevo
