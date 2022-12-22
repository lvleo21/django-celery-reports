# Generated by Django 4.1.4 on 2022-12-22 12:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_realization_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='points',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Pontuação'),
        ),
        migrations.AlterUniqueTogether(
            name='realization',
            unique_together={('account', 'task')},
        ),
    ]