# Generated by Django 2.1.7 on 2020-08-01 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0002_auto_20200728_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='order_sale',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='order_storage',
        ),
        migrations.AddField(
            model_name='delivery',
            name='destination_buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='destination_warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Warehouse'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='source_farmer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deliveryservice',
            name='base_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactionsale',
            name='quantity_from_produce',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='transactionsale',
            name='quantity_from_warehouse',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='type',
            field=models.CharField(choices=[('SD', 'Delivery for Storage'), ('TD', 'Delivery for Sale from Farmer')], max_length=2),
        ),
    ]
