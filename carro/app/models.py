from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
