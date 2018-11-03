from django.contrib import admin
from .models import State,ProducerType,EnergySource,GreenHouseGases

admin.site.register(State)
admin.site.register(ProducerType)
admin.site.register(EnergySource)
admin.site.register(GreenHouseGases)
