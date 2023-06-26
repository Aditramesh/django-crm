
from django.db import models
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.shortcuts import reverse
from .forms import AgentModelForm



class AgentList(LoginRequiredMixin,generic.ListView):
    template_name="agents/agents_list.html"

    def get_queryset(self):
        return Agent.objects.all()
    
class AgentDetail(LoginRequiredMixin,generic.DetailView):
    template_name='agents/agents_detail.html' 
    model=Agent
    # context_object_name='agent'
    # def get_queryset(self):
    #     return Agent.objects.all()

class Agentcreate(LoginRequiredMixin,generic.CreateView):
    template_name='agents/agents_create.html'
    form_class=AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agents-list')
    
class AgentUpdate(LoginRequiredMixin,generic.UpdateView):
    template_name='agents/agent_update.html' 

    model=Agent 
    form_class=AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agents-list')   

    

# Create your views here.
