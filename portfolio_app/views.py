from django.shortcuts import render,redirect
from . models import Contact
from django.http import FileResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method  == "POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        
        Contact.objects.create(name=name,email=email,message=message)
        return redirect('home')
    return render(request, 'index.html')

def download_resume(request):
    file_path='static/ABHIRAJU Resume.pdf (1).pdf'
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename="Abhiraju_Resume.pdf")
