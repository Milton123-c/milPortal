from django.http import HttpResponseRedirect
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail as sm
import json

def index(request):



     return render(request, 'navegacion.html')


def formularioUno(request):

     datos = json.loads(request.body)

     nombre = datos['name']
     mensaje = datos['message']

     res = sm(
        subject = nombre,
        message = mensaje,
        from_email = 'mail@gmail.com',
        recipient_list = ['miltonmercado92@gmail.com'],
        fail_silently=False,
    )  


     return HttpResponseRedirect('/index')


def formularioDos(request):
     
     datos = json.loads(request.body)
     nombre = datos['name']
     mensaje = datos['message']

     res = sm(
        subject = nombre,
        message = mensaje,
        from_email = 'mail@gmail.com',
        recipient_list = ['miltonmercado92@gmail.com'],
        fail_silently=False,
    )   

     return HttpResponseRedirect('/index')


