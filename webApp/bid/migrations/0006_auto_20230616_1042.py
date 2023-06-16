# Generated by Django 2.2.19 on 2023-06-16 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0005_auto_20230616_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='bid',
            field=models.OneToOneField(default='NULL', help_text='Укажите обрабатываемую заявку', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='controls', to='bid.Bid', verbose_name='Заявка'),
        ),
    ]