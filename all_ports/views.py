from django.http import HttpResponse
from django.template import loader

def entryPage(request):
  template = loader.get_template('allPorts.html')
  return HttpResponse(template.render())
