# Generated by Django 2.1.2 on 2018-10-13 22:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrashCan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrashState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('fill_state', models.IntegerField()),
                ('trash_can', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TrashCan')),
            ],
        ),
    ]
