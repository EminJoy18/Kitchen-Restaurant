# Generated by Django 4.1.7 on 2024-02-23 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('Description', models.CharField(max_length=1000)),
                ('Price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Meal_type', models.CharField(choices=[('starters', 'Starters'), ('salads', 'Salads'), ('main_course', 'Main Course'), ('desserts', 'Desserts')], max_length=20)),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updates_at', models.DateTimeField(auto_now=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
