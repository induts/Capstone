from django.http import HttpResponse
from django.shortcuts import render
import datetime

#
def index(request):
     # return HttpResponse("Hello, world. You're at the verde.")
    now = datetime.datetime.now()

    # return HttpResponse(html)
    return render(request, 'verde/index.html')