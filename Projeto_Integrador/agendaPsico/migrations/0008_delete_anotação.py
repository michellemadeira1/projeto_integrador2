# Generated by Django 5.0.3 on 2024-03-27 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendaPsico', '0007_alter_anotação_id_paciente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Anotação',
        ),
    ]
