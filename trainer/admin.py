from django.contrib import admin

# Register your models here.
from trainer import models
#Registrando o modelo Trainer na area admin do Django

@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'cpf', 'data_nascimento', 'created_date',)
    ordering = '-id',
    search_fields = 'first_name', 'last_name', 'cpf',