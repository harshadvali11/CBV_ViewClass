from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.

# responding a string by FBV
def FBV(request):
    return HttpResponse('<h1>This Function based view</h1>')

# responding a string by CBV

class CBV(View):
    def get(self,request):
        return HttpResponse('<h1>This Class based view</h1>')

# Responding a HTML file by using FBV

def FBV_template(request):
    return render(request,'fbv.html',context={'data':'Function Based View context'})

# Responding a HTML file by using CBV

class CBV_template(View):
    def get(self,request):
        return render(request,'cbv.html',context={'data':'Class Based view Context'})

# validate or accepting form data from front end by using FBV

def FBV_form(request):
    form=Student()
    if request.method=="POST":
        form_data=Student(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            #return HttpResponse(form_data.cleaned_data)
    return render(request,'FBV_form.html',context={'form':form})

# validate or accepting form data from front end by using CBV

class CBV_form(View):
    def get(self,request):
        form=Student()
        return render(request,'CBV_form.html',context={'form':form})

    def post(self,request):
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(form_data.cleaned_data['name'])


# dont use View class for html and forms








