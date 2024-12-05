from django.db import models
from django.utils import timezone



#Criando o modelo Trainer

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    
