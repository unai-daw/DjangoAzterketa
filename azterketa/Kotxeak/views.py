from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Kotxea

def kotxeakHTML(request):
  mykotxea = Kotxea.objects.all().values()
  template = loader.get_template('kotxeakHTML.html')
  context = {
    'mykotxea': mykotxea,
  }
  return HttpResponse(template.render(context, request))

def addCoche(request):
  template = loader.get_template('addCoche.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['marca']
  y = request.POST['modelo']
  j = request.POST['matricula']
  k = request.POST['precioHora']
  m = request.POST['alokatzeData']
  mykotxea = Kotxea(marca=x,modelo=y,matricula=j,precioHora=k,alokatzeData=m)
  mykotxea.save()
  mykotxea = Kotxea.objects.all().values()
  template = loader.get_template('kotxeakHTML.html')
  context = {
    'mykotxea': mykotxea,
  }
  return HttpResponse(template.render(context, request))

def deleteCoche(request, id):
  kotxea = Kotxea.objects.get(id=id)
  kotxea.delete()
  mykotxea = Kotxea.objects.all().values()
  template = loader.get_template('kotxeakHTML.html')
  context = {
    'mykotxea': mykotxea,
  }
  return HttpResponse(template.render(context, request))

def updateCoche(request, id):
  mykotxea = Kotxea.objects.get(id=id)
  template = loader.get_template('updateCoche.html')
  context = {
    'mykotxea': mykotxea,
  }
  return HttpResponse(template.render(context, request))

def updaterecordCoche(request, id):
  marca = request.POST['marca']
  modelo = request.POST['modelo']
  matricula = request.POST['matricula']
  precioHora = request.POST['precioHora']
  alokatzeData = request.POST['alokatzeData']
  kotxea = Kotxea.objects.get(id=id)
  
  kotxea.marca = marca
  kotxea.modelo = modelo
  kotxea.matricula = matricula
  kotxea.precioHora = precioHora
  kotxea.alokatzeData = alokatzeData
  kotxea.save()

  mykotxea = Kotxea.objects.all().values()
  template = loader.get_template('kotxeakHTML.html')
  context = {
    'mykotxea': mykotxea,
  }
  return HttpResponse(template.render(context, request))

def bistaratu(request):
  template = loader.get_template('bistaratu.html')
  return HttpResponse(template.render({}, request))

def bistaratu2(request):
  id = request.POST['id']
  kotxea = Kotxea.objects.get(id=id)
  

  data=kotxea.alokatzeData
 
  template = loader.get_template('bistaratu.html')
  return HttpResponse(template.render({'data':data}, request))