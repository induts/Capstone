from django.db import models

class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProducerType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class EnergySource(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class GreenHouseGases(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    energy_source = models.ForeignKey(EnergySource, on_delete=models.PROTECT)
    producer_type = models.ForeignKey(ProducerType, on_delete=models.PROTECT)
    CO2 = models.IntegerField()
    SO2 = models.IntegerField()
    NOx = models.IntegerField()
    year = models.IntegerField()
    def __str__(self):
        return f"{self.state} - {self.producer_type} - {self.CO2} - {self.year}"


