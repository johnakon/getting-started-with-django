from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


# CRUD OPERATIONS - class based views



# landing page as class view
class LandingPageView(TemplateView) :
    template_name = "landing.html"


# lead list as a class using ListView
class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
   

# Detail view as a class using DetailView
class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


# Create view as a class using CreateView
class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    # specific method when form is saved successfully
    def get_success_url(self):  
        # return "/leads"  
        return reverse("leads:lead-list")



# update view as a class using UpdateView
class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    # specific method when form is saved successfully
    def get_success_url(self):  
        # return "/leads"  
        return reverse("leads:lead-list")


# delete view as a class using DEleteView
class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all() 

    # specific method when form is saved successfully
    def get_success_url(self):  
        # return "/leads"  
        return reverse("leads:lead-list")
