from django.shortcuts import render

# Create your views here.

def services(request):
    datas = {
        
    }
    return render(request, 'services.html', datas)

def project(request):
    datas = {
        
    }
    return render(request, 'project.html', datas)

def elements(request):
    datas = {
        
    }
    return render(request, 'elements.html', datas)

def apartment(request):
    datas = {
        
    }
    return render(request, 'Apartment.html', datas)
