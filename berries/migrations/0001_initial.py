# Generated by Django 4.2.2 on 2023-06-30 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='berries_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('berry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berries.berries')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berries.categories')),
            ],
        ),
    ]