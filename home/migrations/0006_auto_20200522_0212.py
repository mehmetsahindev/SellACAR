# Generated by Django 3.0.5 on 2020-05-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200522_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('True', 'True')], default='New', max_length=10),
        ),
    ]
