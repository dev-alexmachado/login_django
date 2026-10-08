from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome