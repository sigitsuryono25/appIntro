import time

from django.http import HttpResponse
from django.shortcuts import render


def daftarAplikasi(self):
    last_path = breadCrumbs(self)
    return render(self, 'admin/list-aplikasi.html', {'current_path': 'Aplikasi > ' + last_path})


def tambahAplikasi(self):
    last_path = breadCrumbs(self)
    id = str(int(round(time.time() * 1000)))
    return render(self, 'admin/tambah-aplikasi.html', {'current_path': 'Aplikasi > ' + last_path, 'id': id})


def tambahAplikasiProses(self):
    return HttpResponse()


def breadCrumbs(self):
    path = self.get_full_path().split('/admins/')
    last_path = path[1].replace('/', ' >')
    return last_path.replace('-', " ")
