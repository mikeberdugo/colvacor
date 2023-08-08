from django.shortcuts import render, redirect
import json



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


def sistema1(request):
    return render(request,"sistema1.html")

def grafica_view(request):
    # Supongamos que estos son los datos para tu gráfica
    data = {
        'labels': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'data': [10, 25, 18, 32, 12],
    }

    data_json = json.dumps(data)

    return render(request, 'grafica.html', {'data_json': data_json})
    return render(request, 'grafica.html', {'labels': labels, 'data': data})
