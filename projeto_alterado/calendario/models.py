from django.db import models

class Squad(models.Model):
    nome       = models.CharField(max_length=100)
    cor        = models.CharField(max_length=15)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class atividades(models.Model):
    titulo     = models.CharField(max_length=80)
    descricao  = models.CharField(max_length=400)
    area       = models.ForeignKey(Squad, on_delete=models.CASCADE)
    data       = models.DateField()
    hora       = models.TimeField()

class FreezingPeriod(models.Model):
     start_date = models.DateField()
     end_date = models.DateField()
     environment_choices = [
         ('card', 'Cartão'),
         ('bank', 'Banco'),
     ]
     environment = models.CharField(max_length=4, choices=environment_choices)
     color = models.CharField(max_length=15)  # Cor representativa do ambiente

     def __str__(self):
         return f"Período de Congelamento: {self.start_date} - {self.end_date}"

