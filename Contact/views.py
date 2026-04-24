from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import Contactform
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'base.html')

def add(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Contact Added Successfully") 
    else:
        form = Contactform()
    return render(request, 'add_contact.html', {'form': form})
  

def contact_list(request):
    if request.method == "GET":
        record = Contact.objects.all()
    return render(request, 'contact_list.html', {'record': record})
            

def update_contact(request,id):
    if request.method == "POST":
        record = Contact.objects.get(pk=id)
        form = Contactform(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
    else:
        record = Contact.objects.get(pk=id)
        form = Contactform(instance=record)
    return render(request, 'edit_contact.html', {'form': form})


def delete_contact(request,id):
    if request.method == "POST":
        record = Contact.objects.get(pk=id)
        record.delete()
    return HttpResponseRedirect('/list/')