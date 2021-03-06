# Generated by Django 3.2.7 on 2021-09-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='order', related_query_name='order-confirmation', to='customer.MenuItem'),
        ),
    ]
