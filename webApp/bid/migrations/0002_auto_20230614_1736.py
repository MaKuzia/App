# Generated by Django 2.2.19 on 2023-06-14 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ('title', 'location'), 'verbose_name': 'Подразделение', 'verbose_name_plural': 'Подразделения'},
        ),
    ]