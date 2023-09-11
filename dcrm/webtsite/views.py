from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import *

# Create your views here.
def home(request):
    #Check to see if logging in
    #POST is information a user submits, like email and password
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU HAVE BEEN LOGGED IN")
            return redirect('home')
        else:
            messages.success(request, 'THERE WAS AN ERROR LOGIN IN')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})

def verify_room(request):
    if request.method == "POST":
        roomcode = request.POST.get("room_code")
        if roomcode == "ola":
            return HttpResponse("<h1>ola</h1>")

class NotasView(APIView):
    serializer_class = NotasSerializer 
    
    def get(self, request):
        detail = [ {"id": detail.auto_increment_id,"title": detail.title,"description": detail.description} 
        for detail in Notas.objects.all()]
        return Response(detail)
    
    def post(self, request):
  
        serializer = NotasSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)