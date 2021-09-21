from django.shortcuts import render
from .models import Operation, Bin

# Create your views here.
operations = Operation.objects.all()

def opfront(request):
    
    bins = Bin.objects.all()

    return render(request, 'binoperations/opfront.html', {'operations':operations, 'bins':bins})

def bins_operations_pair(request):
    
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