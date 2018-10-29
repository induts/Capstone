from django.db import models


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProducerType(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.state.name + ' - ' + self.name

class EnergySource(models.Model):
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    total_population = models.IntegerField()
    percent_female = models.FloatField()

    def __str__(self):
        return self.county.state.name + ' - ' + self.county.name + ' - ' + str(self.total_population)






