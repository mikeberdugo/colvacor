from django.shortcuts import render, redirect ,get_object_or_404
from colvacor.models import *
from colvacor.models import *


def operators_core(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_core.html',{'context' :context })

def operators_nodo(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_nodo.html',{'context' :context })

def operators_gpon(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_gpon.html',{'context' :context })

def operators_nal(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_nal.html',{'context' :context })

def operators_adsl(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_adsl.html',{'context' :context })

def operators_local(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_local.html',{'context' :context })

def operators_iptv(request):
    context = request.session.get('context', {}) 
    return render(request, './operators/operators_iptv.html',{'context' :context })


def operators_mpls(request):
    context = request.session.get('context', {})    
    DesempenoMPLS = Alarmas.objects.filter(Filtro='Filtro: Desempeño MPLS') 
    LSPs_Status = Alarmas.objects.filter(Filtro='Filtro: LSPs y LDPs Status') 
    Subscribers = Alarmas.objects.filter(Filtro='Filtro: Subscribers') 
    Trafico_Interfaces = Alarmas.objects.filter(Filtro='Filtro: TraficoInterfaces') 
    Falla_componentes = Alarmas.objects.filter(Filtro='Filtro: FallaCompMPLS') 
    CGNAt = Alarmas.objects.filter(Filtro='mams') 
    BGP_Rr = Alarmas.objects.filter(Filtro='BGP peer 10.32.0.13') 
    Potencia_Interfaces =  Alarmas.objects.filter(Filtro='uei.opennms.org/translator/ETB/RxPowerInterface') 
    Troncales = Alarmas.objects.filter(Filtro='link') 
    
    return render(request, './operators/operators_mpls.html',{
        'context' :context ,
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

def pagina_no_encontrada(request, ruta_no_definida):
    return render(request, './error-404.html', {'ruta_no_definida': ruta_no_definida})