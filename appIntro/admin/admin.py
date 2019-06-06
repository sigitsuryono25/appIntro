from django.urls import path

from AppIntro.admins import admin_views, aplikasi_views, usermanage_views

urlpatterns = [
    path('login-admins/', admin_views.login),
    path('dashboard/', admin_views.dashboard),
    path('login-proses/', admin_views.login_proses),
    path('logout/', admin_views.logout),
    path('daftar-aplikasi/', aplikasi_views.daftarAplikasi),
    path('tambah-aplikasi/', aplikasi_views.tambahAplikasi),
    path('tambah-aplikasi-proses/', aplikasi_views.tambahAplikasiProses),
    path('daftar-user/', usermanage_views.daftarUser)
]
