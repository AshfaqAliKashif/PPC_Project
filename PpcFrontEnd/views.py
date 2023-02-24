from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def home(request):
	return render(request, 'index.html')