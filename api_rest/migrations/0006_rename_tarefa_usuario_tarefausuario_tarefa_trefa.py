# Generated by Django 5.0.1 on 2024-01-31 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0005_rename_usertasks_tarefausuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefausuario',
            old_name='tarefa_usuario',
            new_name='tarefa_trefa',
        ),
    ]
