# Generated by Django 3.2.18 on 2023-03-06 09:25

from django.db import migrations, models
import order.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_contact', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_dob', models.DateField(blank=True, null=True)),
                ('booking_datetime', models.DateTimeField(blank=True, null=True)),
                ('delivery_datetime', models.DateTimeField(blank=True, null=True)),
                ('total_cost', models.IntegerField(blank=True, null=True)),
                ('advance_payment', models.IntegerField(blank=True, null=True)),
                ('remaining_balance', models.IntegerField(blank=True, null=True)),
                ('frame', models.CharField(blank=True, max_length=200, null=True)),
                ('lens', models.CharField(blank=True, max_length=200, null=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('r_sph', models.CharField(blank=True, max_length=20, null=True)),
                ('r_cyl', models.CharField(blank=True, max_length=20, null=True)),
                ('r_axis', models.CharField(blank=True, max_length=20, null=True)),
                ('l_sph', models.CharField(blank=True, max_length=20, null=True)),
                ('l_cyl', models.CharField(blank=True, max_length=20, null=True)),
                ('l_axis', models.CharField(blank=True, max_length=20, null=True)),
                ('delivered_by', models.CharField(blank=True, max_length=200, null=True)),
                ('checked_by', models.CharField(blank=True, max_length=200, null=True)),
                ('delivered_datetime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[(0, 'PLACED'), (1, 'INPROGRESS'), (2, 'READY'), (3, 'COMPLETED')], default=0, max_length=1)),
                ('tracking_number', models.CharField(blank=True, default=order.helpers.generate_tracking_number, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]