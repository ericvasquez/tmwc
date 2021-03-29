from django.shortcuts import render, redirect
from time import gmtime, strftime
from django.contrib import messages
import bcrypt
from .models import User
# Create your views here.

def index(request):
    return render(request, "index.html")
