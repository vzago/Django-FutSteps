from django.contrib import admin

# Register your models here.
from trainer import models
#Registrando o modelo Trainer na area admin do Django

@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    ...