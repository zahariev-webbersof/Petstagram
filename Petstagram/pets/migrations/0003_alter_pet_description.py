# Generated by Django 3.2.4 on 2021-06-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(),
        ),
    ]
