# Generated by Django 5.0.1 on 2024-01-31 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0004_usertasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userTasks',
            new_name='tarefaUsuario',
        ),
        migrations.RenameField(
            model_name='tarefausuario',
            old_name='user_nickname',
            new_name='tarefa_nickname',
        ),
        migrations.RenameField(
            model_name='tarefausuario',
            old_name='user_task',
            new_name='tarefa_usuario',
        ),
    ]
