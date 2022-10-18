from django.http import HttpResponse
from django.template import loader
from .models import Pertsonak

def pertsonakHTML(request):
  mypertsonak = Pertsonak.objects.all().values()
  template = loader.get_template('pertsonakHTML.html')
  context = {
    'mypertsonak': mypertsonak,
  }
  return HttpResponse(template.render(context, request))

def addPer(request):
  template = loader.get_template('addPer.html')
  return HttpResponse(template.render({}, request))

def addrecordPer(request):
  x = request.POST['izena']
  y = request.POST['abizena']
  pertsona = Pertsonak(izena=x, abizena=y)
  pertsona.save()
  mypertsonak = Pertsonak.objects.all().values()
  template = loader.get_template('pertsonakHTML.html')
  context = {
    'mypertsonak': mypertsonak,
  }
  return HttpResponse(template.render(context, request))

def deletePer(request, id):
  perstona = Pertsonak.objects.get(id=id)
  perstona.delete()
  mypertsonak = Pertsonak.objects.all().values()
  template = loader.get_template('pertsonakHTML.html')
  context = {
    'mypertsonak': mypertsonak,
  }
  return HttpResponse(template.render(context, request))

def updatePer(request, id):
  mypertsonak = Pertsonak.objects.get(id=id)
  template = loader.get_template('updatePer.html')
  context = {
    'mypertsonak': mypertsonak,
  }
  return HttpResponse(template.render(context, request))

def updaterecordPer(request, id):
  izena = request.POST['izena']
  abizena = request.POST['abizena']

  pertsona = Pertsonak.objects.get(id=id)
  pertsona.izena = izena
  pertsona.abizena = abizena
  pertsona.save()

  mypertsonak = Pertsonak.objects.all().values()
  template = loader.get_template('pertsonakHTML.html')
  context = {
    'mypertsonak': mypertsonak,
  }
  return HttpResponse(template.render(context, request))

