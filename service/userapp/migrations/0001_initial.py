# Generated by Django 3.1.3 on 2021-03-02 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]
