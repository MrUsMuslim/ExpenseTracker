# Generated by Django 5.0.7 on 2024-07-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='typeof',
            field=models.CharField(choices=[('food', 'Food'), ('transportation', 'Transportation'), ('savings', 'Savings'), ('housing_and_utilities', 'Housing and utilities'), ('clothing', 'Clothing'), ('other', 'Others')], default='food', max_length=21),
        ),
    ]
