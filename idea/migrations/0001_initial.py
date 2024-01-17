# Generated by Django 4.1 on 2024-01-16 11:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='아이디어명')),
                ('content', models.TextField(max_length=5000, verbose_name='아이디어 설명')),
                ('image', models.ImageField(blank=True, upload_to='idea/', verbose_name='이미지')),
                ('interest', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='아이디어 관심도')),
                ('pick', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.devtool')),
            ],
        ),
    ]
