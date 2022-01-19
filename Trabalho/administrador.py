from django.contrib import admin

from .modelos import *


admin.site.register(Utente)
admin.site.register(Funcionario)
admin.site.register(Medicamentos)
admin.site.register(Utilizador)
admin.site.register(Consulta)
admin.site.register(Prescrição)