from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import datetime
from .models import EnergySource,ProducerType,GreenHouseGases,State

#
def index(request):
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

    #  return render(request, 'verde/index2.html',{'EnergySource':out_sources,'ProducerType': out_types,'State':out_states,'Greenhousegas':out_greengas})
    return render(request, 'verde/index2.html',{'EnergySource':out_sources,'ProducerType': out_types,'State':out_states,'Year':year,'GreenhouseGas':ghgas} )

# def get_data(request):
#     print(request)
#     data = json.loads(request.body)
#     state_obj = State.objects.get(pk=data['state'])
#     energy_obj = EnergySource.objects.get(pk=data['EnergySource'])
#     ptype_obj = ProducerType.objects.get(pk=data['ProducerType'])
#     gas = GreenHouseGases.objects.all()
#     print(f" the gases are {gas}")
#     if show_obj != None:
#         people = people.filter(fav_tv=show_obj)
#     print(f"after first filter {people}")
#     if color_obj != None:
#         people = people.filter(fav_color=color_obj)
#     print(f"after second filter {people}")
#     data = {'people': []}
#     for person in people:
#         data['people'].append({'name': person.name})
#     return JsonResponse(data)



def get_data(request):
    # get the filter parameters from the query string
    #    localhost:8000?energy_source_id=3&producer_type_id=1
    #    request.GET['energy_source_id']
    # use the filter parameters to filter the data
    # convert the data into a list of dictionaries
    # return it in a json response
    gender_id = request.GET['gender_id']
    return JsonResponse({'message': 'ok'})

