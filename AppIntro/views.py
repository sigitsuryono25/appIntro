import datetime

from django.shortcuts import render

# Create your views here.

def index(self):
    date = str(datetime.date.today().year)
    return render(self, 'index.html', {'date' : date})
