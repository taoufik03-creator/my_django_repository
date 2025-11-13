from django.shortcuts import render

# Create your views here.

from .models import Phone
from .forms import PhoneForm

def home_view(request):
    return render(request,"home.html")

def phone_list(request):
    form=PhoneForm()
    phones=Phone.objects.all()
    if request.method=="POST":
        form=PhoneForm(request.POST)
        if form.is_valid():
            form.save()
    content={
        "form":form,
        "phones":phones
    }
    return render(request,"phone_list.html",content)

def phone_details(request,phone_id):
    phone=Phone.objects.get(phone_id=phone_id)
    form=PhoneForm(instance=phone)
    if request.method=="POST":
        form=PhoneForm(request.POST,instance=phone)
        if form.is_valid():
            form.save()
    
    content={
        "phone":phone,
        "form":form
    }

    return render(request,"phone_details.html",content)