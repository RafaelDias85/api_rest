from django.db import models

class Usuarios(models.Model):
    usuario_nickname = models.CharField(primary_key=True, max_length=100, default='')
    usuario_nome = models.CharField(max_length=150, default='')
    usuario_email = models.EmailField(default='')
    usuario_idade = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.usuario_nickname} | E-mail: {self.usuario_email}'
    
