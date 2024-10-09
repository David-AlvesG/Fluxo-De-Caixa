from django.db import models

class Lancamento(models.Model):
    TIPO_CHOICES = (
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
    )
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    data = models.DateField()  # Esta linha adiciona a data automaticamente e não é editável.

    def __str__(self):
        return f"{self.tipo} - {self.valor} - {self.descricao} - {self.data}"
