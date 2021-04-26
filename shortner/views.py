from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method=='POST':
        linkVar = request.POST['link']
        uuidvar = str(uuid.uuid4())[:5]
        urlcreated = Url(link = linkVar, uniqueId = uuidvar)
        urlcreated.save()
        return HttpResponse(uuidvar)


def run(request,pk):
    urldetails = Url.objects.get(uniqueId=pk)
    return redirect('https:/'+urldetails.link)