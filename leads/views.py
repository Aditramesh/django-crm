from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm

def landing_page(request):
   return render(request,'landing.html')

def leads_list(request):
   print(request)
   leads=Lead.objects.all()
   context={
      'leads':leads
    }
   return render(request,'leads/leads.html',context)

def lead_detail(request,pk):
   print(pk)
   print(request)
   lead=Lead.objects.get(id=pk)
   print(lead)
   context={
      'lead':lead,
      'pk':pk
   }
   return render(request,"leads/lead_detail.html",context)
def lead_create(request):
   form=LeadModelForm()
   if request.method=='POST':
      print(request)
      form=LeadModelForm(request.POST)
      print('recieving a post request')
      if form.is_valid():
          form.save()
          return redirect('/leads')      
     

  
   context={
      'form':form
   }
   return render(request,'leads/lead_create.html',context)


def lead_update(request,pk):
   lead=Lead.objects.get(id=pk)
   form=LeadModelForm(instance=lead)
  
  
   if request.method=='POST':
      print(request)
      form=LeadModelForm(request.POST,instance=lead)
      print('recieving a post request')
      if form.is_valid():
          form.save()
          return redirect('/leads')  
   lead=Lead.objects.get(id=pk)
   context={
      'lead':lead,
      'form':form

   }
   return render(request,'leads/lead_update.html',context)

def lead_delete(request,pk):
   print(request)
   lead=Lead.objects.get(id=pk)
   lead.delete()
   return redirect('/leads')


# def lead_create(request):
#    form=LeadForm()
#    if request.method=='POST':
#       form=LeadForm(request.POST)
#       print('recieving a post request')
#       if form.is_valid():
#           print('form is valid')
#           print(form.cleaned_data)
#           first_name=form.cleaned_data['first_name']
#           last_name=form.cleaned_data['last_name']
#           age=form.cleaned_data['age']
#           agent=Agent.objects.first()
#           Lead.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             age=age,
#             agent=agent
#         )
#           return redirect('/leads')      
     

  
#    context={
#       'form':form
#    }
#    return render(request,'leads/lead_create.html',context)
   

