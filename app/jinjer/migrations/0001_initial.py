# Generated by Django 3.0.7 on 2020-06-14 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='メイン項目名')),
                ('datetime', models.DateTimeField(verbose_name='日付')),
            ],
            options={
                'db_table': 'mainlist',
            },
        ),
        migrations.CreateModel(
            name='SubList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='サブ項目名')),
                ('totalnum', models.IntegerField(default=0, verbose_name='総数')),
                ('mainlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinjer.MainList')),
            ],
            options={
                'db_table': 'sublist',
            },
        ),
    ]