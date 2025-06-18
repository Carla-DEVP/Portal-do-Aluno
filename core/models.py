from django.db import models
from django.contrib.auth.models import AbstractUser


# Usuário base (herdando do User padrão se quiser, ou criando um simples)
class Usuario(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('admin', 'Administrador'),
    ]

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    matricula = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()
    foto_perfil = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.usuario.nome


class Professor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    titulacao = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    foto_perfil = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.usuario.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    ano = models.IntegerField()
    semestre = models.IntegerField()

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}"


class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    avaliacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f"{self.matricula} - {self.avaliacao}"


class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.descricao} - {self.status}"


class Aviso(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateField()
    publico_alvo = models.CharField(max_length=50)  # aluno, professor, todos

    def __str__(self):
        return self.titulo


class Documento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    arquivo_url = models.CharField(max_length=500)
    data_upload = models.DateField()

    def __str__(self):
        return self.nome


