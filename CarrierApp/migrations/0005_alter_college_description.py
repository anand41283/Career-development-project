# Generated by Django 4.1.5 on 2024-03-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarrierApp', '0004_alter_login_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='Description',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
