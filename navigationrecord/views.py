from django.shortcuts import render
from.models import NavigationRecord
from datetime import datetime, timedelta
import json

# Create your views here.
def homepage(request):
    return render(request, 'navigationrecord/homepage.html')

def front(request):
    navRecs = NavigationRecord.objects.all()
    
    return render(request, 'navigationrecord/front.html', {'navRecs':navRecs})

def get_two_days_data(request):
    
    timeInterval = datetime.now() - timedelta(hours=48)
    results = NavigationRecord.objects.filter(datetime__gt=timeInterval)

    block = {}
    last_points = []
    for result in results:
        block = {'latitude': result.latitude, 
                'longitude': result.longitude, 
                'vehicle_plate': result.vehicle.plate, 
                'datetime': result.datetime.strftime('%d.%m.%Y, %H:%M:%S')}
        
        last_points.append(block)
        
    print('last_points = ' + json.dumps(last_points, sort_keys=False, indent=4))


    return render(request, 'navigationrecord/twodaysdata.html', {'last_points':last_points})