# evrekaDjangoProject

**Q1 - Navigation Records**

![95b3cfc5b0d915677103cbc90a02aa57](https://user-images.githubusercontent.com/77352442/134175675-643d9b18-fd80-4a85-ac76-88a58e87aa99.gif)

Using the NavigationRecord and Vehicle classes, tried to create a function that returns the list of last points of vehicles in the last 48 hours.

Models can be seen in navigationrecord > models.py

The function can be seen in navigationrecord > views.py

```python
from django.shortcuts import render
from.models import NavigationRecord
from datetime import datetime, timedelta
import json

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
```
And the output is:


```python
last_points = [
    {
        "latitude": 32.38,
        "longitude": 33.36,
        "vehicle_plate": "32 KLM 12",
        "datetime": "19.09.2021, 16:10:38"
    },
    {
        "latitude": 29.34,
        "longitude": 32.33,
        "vehicle_plate": "35 MNO 17",
        "datetime": "19.09.2021, 16:11:22"
    },
    {
        "latitude": 34.32,
        "longitude": 31.33,
        "vehicle_plate": "35 MNO 17",
        "datetime": "20.09.2021, 12:11:58"
    }
]
```


            
----     



**Q2 - Bins and Operations**

![01fc5d038f18981c7fe7d3e8d1e7508f](https://user-images.githubusercontent.com/77352442/134175797-a4cb2113-a71a-4c90-afab-f7ab9b3d9fba.gif)


A simple database model design is expected. According to existing models tried to interact models each other and created a function that shows frequency values for Bin - Operation pairs.

Models can be found in binoperations > models.py
The variety of models can be increased by adding Vehicle, HumanResource models etc.

The function -with a tiny bug :) - shows the interactions between bins and operations can be found in binoperations > views.py

```python
from django.shortcuts import render
from .models import Operation, Bin


def bins_operations_pair(request):
    
    operations = Operation.objects.all()
    block = {}
    list = []
    for operation in operations:
        block = {'bin_id': operation.bin.id,
                'op_name': operation.name,
                'total_frequency': operation.bin.collection_frequency}
        
        list.append(block)

    pairList = []
    for element in list:
        numOfElement = list.count(element)
        m = numOfElement
        while numOfElement > 1:
            list.remove(element)
            numOfElement -= 1
        
        element['operation_frequency'] = m
        pairList.append(element)

    print(pairList)

    return render(request, 'binoperations/binoppair.html', {'pairList':pairList})
```
And the output is:


```python
pairList = [
    {
        "bin_id": 1,
        "op_name": "collect",
        "total_frequency": 6,
        "operation_frequency": 2
    },
    {
        "bin_id": 1,
        "op_name": "extinguish",
        "total_frequency": 6,
        "operation_frequency": 2
    },
    {
        "bin_id": 1,
        "op_name": "move",
        "total_frequency": 6,
        "operation_frequency": 2
    },
    {
        "bin_id": 2,
        "op_name": "collect",
        "total_frequency": 3,
        "operation_frequency": 3
    },
    {
        "bin_id": 3,
        "op_name": "move",
        "total_frequency": 3,
        "operation_frequency": 2
    },
    {
        "bin_id": 3,
        "op_name": "collect",
        "total_frequency": 3,
        "operation_frequency": 1
    },
    {
        "bin_id": 4,
        "op_name": "collect",
        "total_frequency": 4,
        "operation_frequency": 3
    },
    {
        "bin_id": 4,
        "op_name": "collect",
        "total_frequency": 4,
        "operation_frequency": 1
    }
]
```




