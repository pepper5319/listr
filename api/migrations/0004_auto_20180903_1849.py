# Generated by Django 2.1.1 on 2018-09-03 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20180903_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('static_id', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True, max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='listobject',
            name='collaborators',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='assigned_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ListObject'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
