# Generated by Django 4.2.4 on 2024-04-10 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_dish_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='tablereservation',
            name='table_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.table'),
        ),
    ]
