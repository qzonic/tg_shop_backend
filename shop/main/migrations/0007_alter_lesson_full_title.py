# Generated by Django 3.2.18 on 2023-03-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20230316_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='full_title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
