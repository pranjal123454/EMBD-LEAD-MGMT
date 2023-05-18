
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead,Resource,Upcoming_Lead,LeadAction
from .forms import LeadForm,LeadModelForm,Upcoming_LeadModelForm,Upcoming_LeadForm

# Create your views here.
def lead_list(request):
    leads=Lead.objects.all()

    context={
       "leads":leads
    }
    return render(request,'leads/lead_list.html',context)

def lead_details(request,pk):
    lead=Lead.objects.get(id=pk)
    context1={
       "lead":lead
    }
    return render(request,'leads/lead_detailed.html',context1)

def lead_create(request):
    form=LeadModelForm()
    if(request.method=="POST"):
      form=LeadModelForm(request.POST)
      if form.is_valid():
          form.save()
         #  first_name=form.cleaned_data['first_name']
         #  last_name=form.cleaned_data['last_name']
         #  age=form.cleaned_data['age']
         #  agent=form.cleaned_data['agent']
         #  Lead.objects.create(first_name=first_name,last_name=last_name,age=age,agent=agent)
          return redirect("/leads")
      print("recevibg a post request")
    context={
       "form":form
    }
    return render(request,'leads/lead_create.html',context)



def LeadUpdate(request,pk):
    lead=Lead.objects.get(id=pk)
    form=LeadModelForm( instance=lead)
    if(request.method=="POST"):
      form=LeadModelForm(request.POST,instance=lead)
      if form.is_valid():
          form.save()
         
          return redirect("/leads")

    context={
        "form":form,
        "lead":lead
    }
    return render(request,'leads/lead_update.html',context)


def leadDelete(request,pk):
    lead=Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

def landing_page(request):
    return render(request,'leads/landing_page.html')









# Lead management
def Upcoming_Lead_Create(request):
    form=Upcoming_LeadModelForm()
    if(request.method=="POST"):
      form=Upcoming_LeadForm(request.POST)
      if form.is_valid():
        #   form.save()
          name=form.cleaned_data['name']
          email=form.cleaned_data['email']
          phone_number=form.cleaned_data['phone_number']
          country=form.cleaned_data['country']
          lead_description=form.cleaned_data['lead_description']
          Upcoming_Lead.objects.create(name=name,email=email,phone_number=phone_number,lead_description=lead_description,country=country)
          return redirect("/leads")
      print("recevibg a post request")
    context={
       "form":form
    }
    return render(request,'leads/Upcoming_Lead_Create.html',context)

