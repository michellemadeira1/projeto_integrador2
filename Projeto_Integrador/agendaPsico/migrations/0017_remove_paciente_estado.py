# Generated by Django 5.0.6 on 2024-05-14 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendaPsico', '0016_remove_agenda_data_anotação_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='estado',
        ),
    ]
