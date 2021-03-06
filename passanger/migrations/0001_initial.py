# Generated by Django 3.2 on 2022-03-11 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recet_number', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Trip', to='manager.trip')),
            ],
            options={
                'ordering': ['-date_published'],
            },
        ),
    ]
