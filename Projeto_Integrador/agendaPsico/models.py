from django.db import models


# Create your models here.
class Paciente(models.Model):
    nome_paciente = models.CharField(max_length=200)
    nascimento_paciente = models.DateField(blank=True)
    telefone_paciente = models.CharField(max_length=11, blank=True)
    responsável = models.CharField(max_length=200, blank=True)
    endereço = models.CharField(max_length=300, blank=True)
    número = models.CharField(max_length=11, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    início_tratamento = models.DateField(blank=True, null=True)
    término_tratamento = models.DateField(blank=True, null=True) 

    def __str__(self):
        return self.nome_paciente

class Anotação(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    registro = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class Agenda(models.Model):
    tarefa = models.TextField(blank=True, null=True)
    data_tarefa = models.DateField(blank=True, null=True)
    