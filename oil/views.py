from django.shortcuts import render

from .models import Oilio
#
def index(request):
    oild = Oilio.objects.all()
    return render(request, 'oil/index.html', {'oild' : oild})