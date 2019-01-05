# Generated by Django 2.1.5 on 2019-01-05 13:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcan',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trashstate',
            name='fill_state',
            field=models.FloatField(),
        ),
    ]
