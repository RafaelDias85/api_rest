# Generated by Django 5.0.1 on 2024-01-31 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0003_delete_usertasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='userTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nickname', models.CharField(default='', max_length=100)),
                ('user_task', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
