# Generated by Django 2.1.7 on 2019-05-09 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInFo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('age', models.IntegerField(blank=True)),
                ('profession', models.CharField(blank=True, max_length=100)),
                ('hobby', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('weiChat', models.CharField(blank=True, max_length=100)),
                ('skills', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='account/')),
            ],
        ),
    ]
