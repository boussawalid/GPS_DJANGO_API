from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import GPSData
from datetime import datetime

@csrf_exempt
def receive_gps_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            latitude = float(data.get('latitude'))
            longitude = float(data.get('longitude'))
            date_str = data.get('date')
            time_str = data.get('time')

            # Conversion en objets datetime
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            time_obj = datetime.strptime(time_str, '%H:%M:%S').time()

            # Sauvegarde en base de données
            GPSData.objects.create(
                latitude=latitude,
                longitude=longitude,
                date=date_obj,
                time=time_obj
            )

            return JsonResponse({'status': 'success', 'message': 'Données GPS enregistrées !'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)
