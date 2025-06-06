# Generated by Django 5.2 on 2025-05-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfound', '0005_alter_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='disposition',
            field=models.CharField(blank=True, choices=[('Return', 'Return'), ('Donated', 'Donated'), ('Not claimed', 'Not claimed')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('Lost', 'Lost'), ('Found', 'Found')], default='lost', max_length=10),
        ),
    ]
