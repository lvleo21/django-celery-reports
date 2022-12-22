# Generated by Django 4.1.4 on 2022-12-22 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_task_segmentation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('points', models.PositiveIntegerField(blank=True, default=0, verbose_name='Pontos')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization', verbose_name='Organização')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task', verbose_name='Ação')),
            ],
            options={
                'verbose_name': 'Realização',
                'verbose_name_plural': 'Realizações',
            },
        ),
    ]