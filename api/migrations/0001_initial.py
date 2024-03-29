# Generated by Django 4.2.7 on 2024-01-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField(default=1)),
                ('spec', models.CharField(choices=[('6gb-128gb', '6gb-128gb'), ('8gb-256gb', '8gb-256gb')], default='6gb-128gb', max_length=200)),
            ],
        ),
    ]
