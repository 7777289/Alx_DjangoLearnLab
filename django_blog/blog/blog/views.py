from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'base.html', {'year': datetime.now().year})
