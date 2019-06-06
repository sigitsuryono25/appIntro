from django.shortcuts import render


def daftarUser(self):
    return render(self, 'admin/list-user.html', {})