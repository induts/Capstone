from django.core.management.base import BaseCommand
import csv
import os
os.environ['DJANGO_SETTINGS_MODULE']= 'mysite.settings'
import django
django.setup()

# def parse_csv(path):
#     with open(path, 'r') as f:
#         lines = f.read().split('\n')
#     headers = lines[0].split(',')
#     lines.pop(0)
#     data = []
#     for line in lines:
#         if line == '':
#             continue
#         row_data = {}
#         row_data_text = line.split(',')
#         for i in range(len(headers)):
#             row_data[headers[i]] = row_data_text[i]
#         data.append(row_data)
#     return data

from verde.models import State,ProducerType,EnergySource,GreenHouseGases
class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_path = 'C:\\Users\\indut\\Capstone\\mysite\\verde\\management\\commands\\emissionannual.csv'
        data = []
        headers = None
        with open(csv_path, newline='') as csvfile:
            input_data = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(input_data):
                # print(i, row)
                if i == 0:
                    headers = row
                    # print(headers)
                    continue
                row_data = {}
                for i in range(len(headers)):
                    row_data[headers[i]] = row[i].replace(',', '')

                data.append(row_data)

        # Steps to put data in database
        GreenHouseGases.objects.all().delete()

        for datum in data:

              # get or create if it doesn't exist
                state_name = datum['State']
                if not State.objects.filter(name=state_name).exists():
                    state = State(name=state_name)
                    state.save()
                else:
                    state = State.objects.get(name=state_name)

                ProducerType_name = datum['Producer Type']
                if not ProducerType.objects.filter(name=ProducerType_name).exists():
                    producerType = ProducerType(name=ProducerType_name)
                    producerType.save()
                else:
                    producerType = ProducerType.objects.get(name=ProducerType_name)

                EnergySource_name = datum['Energy Source']
                if not EnergySource.objects.filter(name=EnergySource_name).exists():
                    energeysource = EnergySource(name=EnergySource_name)
                    energeysource.save()
                else:
                    energeysource = EnergySource.objects.get(name=EnergySource_name)
                # cd = CensusDatum(county=county, total_population=total_population, percent_female=percent_female)
                # cd.save()



                state_name = datum['State']
                in_state = State.objects.get(name=state_name)
                ProducerType_name = datum['Producer Type']
                in_pro = ProducerType.objects.get(name=ProducerType_name)
                EnergySource_name = datum['Energy Source']
                in_ener = EnergySource.objects.get(name=EnergySource_name)
                ghg = GreenHouseGases(state=in_state,producer_type=in_pro,energy_source=in_ener,CO2=datum["CO2"],SO2=datum["SO2"],NOx=datum['NOx'],year=datum['Year'] )
                ghg.save()
