from django.shortcuts import render, redirect
#from .forms import *
import MySQLdb
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
    return render(request, 'formulario.html')
