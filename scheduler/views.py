from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import scraping


def index(request):

    return render(request, "scheduler/index.html")

#execute function
def execute(request):
    if request.method=='POST':
        id = request.POST["id"]
        pswd = request.POST["pswd"]
        html = scraping.getPageSource(id, pswd) #don't commit leave the password
        dict_data = scraping.exportAsDict(html)
    return render(request, "scheduler/index.html", dict_data)
