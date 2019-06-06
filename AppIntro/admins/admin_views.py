from django.http import HttpResponse
from django.shortcuts import render, redirect

from AppIntro.models import Admin


def login(self):
    return render(self, 'admin/authentication-login.html', {})


def dashboard(self):
    last_path = breadCrumbs(self)
    if isLoggedIn(self):
        return render(self, 'admin/dashboard.html', {'current_path': last_path})
    else:
        return HttpResponse(
            "You're not log in. Clicked <a href='{0}'>here</a> to login".format('/admins/login-admins/'))


def login_proses(self):
    username = self.POST['username']
    password = self.POST['passwd']

    result = Admin.objects.filter(username=username, passwords=password).exists()
    self.session['username'] = username
    # return HttpResponse(self.session['username'])
    if result:
        self.session['username'] = username
        return redirect('/admins/dashboard/')
    else:
        return HttpResponse()


def isLoggedIn(self):
    if 'username' not in self.session:
        return False
    else:
        return True


def logout(self):
    self.session.flush()
    return redirect(login)


def breadCrumbs(self):
    path = self.get_full_path().split('/admins/')
    last_path = path[1].replace('/', ' >')
    return last_path.replace('-', " ")
