# Generated by Django 2.2.1 on 2019-06-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('passwords', models.CharField(max_length=100)),
                ('last_loggedin', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id_apps', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('judul_apps', models.CharField(max_length=100)),
                ('deskripsi_satu', models.CharField(default='', max_length=100)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(default='', on_delete=False, to='AppIntro.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Subjudul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjudul', models.CharField(max_length=100)),
                ('deskripsi_subjudul', models.CharField(default='', max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(default='', on_delete=False, to='AppIntro.Admin')),
                ('id_apps', models.ForeignKey(on_delete=False, to='AppIntro.Apps')),
            ],
        ),
        migrations.CreateModel(
            name='Fitur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_fitur', models.CharField(max_length=100)),
                ('deskripsi_fitur', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(default='', on_delete=False, to='AppIntro.Admin')),
                ('id_apps', models.ForeignKey(on_delete=False, to='AppIntro.Apps')),
            ],
        ),
    ]
