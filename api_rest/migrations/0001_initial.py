# Generated by Django 5.0.1 on 2024-01-31 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario_nickname', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('usuario_nome', models.CharField(default='', max_length=150)),
                ('usuario_email', models.EmailField(default='', max_length=254)),
                ('usuario_idade', models.IntegerField(default=0)),
            ],
        ),
    ]