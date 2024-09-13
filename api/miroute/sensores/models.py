
from django.db import models

class DadosSensor(models.Model):
    id = models.AutoField(primary_key=True)  
    timestamp = models.DateTimeField(auto_now_add=True)
    temperatura = models.FloatField(null=True, blank=True) 
    teor_gordura = models.FloatField(null=True, blank=True)  
    ph = models.FloatField(null=True, blank=True) 
    data_coleta = models.DateField(null=True, blank=True)  
    hora_coleta = models.TimeField(null=True, blank=True)  
    informacoes_adicionais = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"ID: {self.id} - Data: {self.data_coleta} Hora: {self.hora_coleta} - Temp: {self.temperatura}°C, Gordura: {self.teor_gordura}%, pH: {self.ph}"
    