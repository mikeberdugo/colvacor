from django.shortcuts import render, redirect


#### loging 
def inicio(request):
    error_message = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin' : 
            return redirect(sistema1)
        else :
            error_message.append( "Nombre de usuario o contraseña incorrectos.")
    return render(request,"index.html",{'error_message': error_message})

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


def sistema3(request):
    
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
    return render(request,"./admin/admin_usuarios.html")

#### plantilla --- nuevo 
def nuevo(request):    
    return render(request,"./admin/nuevo_usuario.html")

#### plantilla --- alarmas descartadas 
def alarmas(request):    
    return render(request,"./admin/alarma.html")


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


