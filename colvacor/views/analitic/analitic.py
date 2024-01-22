import httpx
from django.http import JsonResponse
from colvacor.models import Alarmas
import datetime
import json
import asyncio

def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def mpls_analysis(request):
    # Obtener datos específicos del modelo directamente con values
    aux = Alarmas.objects.values("Event_ID", "Severity", "Event_Time", "Node_Name", "Filtro")
    
    # Convertir las fechas a un formato específico (puedes ajustar el formato según tus necesidades)
    aux = list(aux)
    for item in aux:
        event_time = item['Event_Time']
        if event_time and isinstance(event_time, str):
            # Convierte la cadena a un objeto de fecha si es una cadena
            item['Event_Time'] = datetime.datetime.strptime(event_time, '%Y-%m-%d %H:%M:%S.%f')
        elif event_time:
            # Formatea la fecha si ya es un objeto de fecha
            item['Event_Time'] = event_time.strftime('%Y-%m-%d %H:%M:%S')

    
    # Combina todos los elementos en un solo diccionario
    combined_data = {key: [item[key] for item in aux] for key in aux[0]}

    # Crear la URL de la API de FastAPI
    fastapi_url = "http://192.168.56.1:8000/analysis"  #! Reemplaza con la URL real
    #http://192.168.56.1:8000/docs#/
    # Enviar los datos a la API en FastAPI
    async def send_data():
        async with httpx.AsyncClient() as client:
            response = await client.post(
                fastapi_url, 
                data=json.dumps(combined_data, default=serialize_datetime)
            )
        return response.json()

    # Ejecutar la función asíncrona y obtener la respuesta
    response_data = asyncio.run(send_data())

    # Devolver los datos de la API de FastAPI como una respuesta JsonResponse
    return JsonResponse(response_data, safe=False)