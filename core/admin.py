from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Nota)
admin.site.register(Pagamento)
admin.site.register(Aviso)
admin.site.register(Documento)

