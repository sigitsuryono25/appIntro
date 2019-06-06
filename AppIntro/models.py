from django.db import models


# Create your models here.

class Apps(models.Model):
    id_apps = models.IntegerField(null=False, primary_key=True, unique=True)
    judul_apps = models.CharField(max_length=100, null=False)
    deskripsi_satu = models.CharField(max_length=100, default="")
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    added_by = models.ForeignKey('Admin', on_delete=False, null=False, default="")


class Subjudul(models.Model):
    id_apps = models.ForeignKey('Apps', on_delete=False)
    subjudul = models.CharField(max_length=100, null=False)
    deskripsi_subjudul = models.CharField(max_length=255, default="")
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    added_by = models.ForeignKey('Admin', on_delete=False, null=False, default="")


class Fitur(models.Model):
    id_apps = models.ForeignKey('Apps', on_delete=False)
    judul_fitur = models.CharField(max_length=100, null=False)
    deskripsi_fitur = models.CharField(max_length=255, null=False)
    added_on = models.DateTimeField(auto_now_add=True, blank=True)
    added_by = models.ForeignKey('Admin', on_delete=False, null=False, default="")


class Admin(models.Model):
    username = models.CharField(max_length=100, null=False, primary_key=True, unique=True)
    passwords = models.CharField(max_length=100, null=False)
    last_loggedin = models.DateTimeField(auto_now_add=True, blank=True)
