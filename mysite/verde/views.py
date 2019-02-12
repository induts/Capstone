from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import datetime
from .models import EnergySource,ProducerType,GreenHouseGases,State
import json
#

def home(request):
    return render(request, 'verde/Home.html', {})


def about(request):
    return render(request, 'verde/about.html', {})

def chart(request):
    sources = EnergySource.objects.all()
    out_sources = []
    for source in sources:
        out_sources.append(source)
    print(out_sources)

    producertypes = ProducerType.objects.all()
    out_types = []
    for producertype in producertypes:
        out_types.append(producertype)
    print(out_types)

    states= State.objects.all()
    out_states = []
    for state in states:
        out_states.append(state)
    print(out_states)

    year_lower = 1990
    year_upper = 2017
    year =[]
    for i in range(year_lower,year_upper,1):
        year.append(i)
    print(year)

    ghgas=['CO2','SO2','NOx']
    print(ghgas)

    # greenhousegase = GreenHouseGases.objects.all()
    # out_greengas =[]
    # for gas in greenhousegase:
    #     out_greengas.append(gas)
    # print(out_greengas)


    return render(request, 'verde/chart.html',{'EnergySource':out_sources,'ProducerType': out_types,'State':out_states,'Year':year,'GreenhouseGas':ghgas} )

def get_data(request):
    # get the filter parameters from the query string
    #    localhost:8000?energy_source_id=3&producer_type_id=1
    #    request.GET['energy_source_id']
    # use the filter parameters to filter the data
    # convert the data into a list of dictionaries
    # return it in a json response
    producer_type_id =request.GET.get('producertype', '')
    energy_source_id = request.GET.get('energysource', '')
    state_id = request.GET.get('state'
                               '', '')
    items=GreenHouseGases.objects.all()
    print(producer_type_id)

    if producer_type_id != '':
        items = items.filter(producer_type_id=producer_type_id)
    if energy_source_id != '':
        items = items.filter(energy_source_id=energy_source_id)
    else:
        items = items.filter(energy_source_id=1)
    if state_id != '':
        items = items.filter(state_id=state_id)

    items = items[:100]
    print(items)

    data = []
    for item in items:
        data.append(item.to_dictionary())
    return JsonResponse({'data': data})
