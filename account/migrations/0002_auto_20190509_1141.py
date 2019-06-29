# Generated by Django 2.1.7 on 2019-05-09 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hobby',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(null=True, upload_to='account/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weiChat',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
