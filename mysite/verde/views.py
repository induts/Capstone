from django.http import HttpResponse
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
    ptypes = ProducerType.objects.all()
    out_types = []
    for ptype in types:
        out_types.append(ptypes)
    print(out_types)
    # return HttpResponse(html)
    return render(request, 'verde/index2.html',{'EnergySource':out_sources},{'ProducerType': out_types})


