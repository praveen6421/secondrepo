from django.shortcuts import render

from .models import EnquiryFormData
from .forms import EnquiryForm
from django.http.response import HttpResponse

def enquiryform_view(request):
    if request.method == 'POST':
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
           firstname = request.POST.get('firstname','')
           lastname = request.POST.get('lastname','')
           email = request.POST.get('email','')
           mobile = request.POST.get('mobile','')
           qualification = request.POST.get('qualification','')
           location = request.POST.get('location','')

           data = EnquiryFormData(
               firstname = firstname,
               lastname = lastname,
               email = email,
               mobile = mobile,
               qualification = qualification,
               location = location,
           )
           data.save()
           eform=EnquiryForm()
           return render(request,'enquiryform.html',{'eform':eform})
        else:
            return HttpResponse("Please Check Given Data.Some Data Missed.")
    else:
        eform = EnquiryForm()
        return render(request,'enquiryform.html',{'eform':eform})