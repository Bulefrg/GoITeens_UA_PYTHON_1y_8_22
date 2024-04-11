# Generated by Django 4.2.4 on 2024-04-10 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_dish_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablereservation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='tablereservation',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='tablereservation',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='tablereservation',
            name='user_profile',
            field=models.ForeignKey(default=555333, on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile'),
            preserve_default=False,
        ),
    ]
