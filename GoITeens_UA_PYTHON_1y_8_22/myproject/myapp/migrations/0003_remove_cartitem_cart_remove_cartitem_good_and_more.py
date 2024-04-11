# Generated by Django 4.2.4 on 2024-04-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cart_alter_good_id_alter_good_image_alter_good_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='good',
        ),
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]