from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


# lead list
def lead_list(request):

    # fetch all leads and store in a variable leads
    leads = Lead.objects.all()

    context={
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)


# leads details
# a primary key is also passed
def lead_detail(request, pk):
    # print(pk)
    lead = Lead.objects.get(id=pk)
    # print(lead)
    context = {
        "lead" : lead
    }
    return render(request, "leads/lead_detail.html", context)


# creating a lead from 
def lead_create(request):
    form = LeadModelForm()  # empty form instantiation
    # print(request.POST)

    # check if method is POST 
    if request.method == "POST":
        print("Receiving a post request")
        form = LeadModelForm(request.POST)
        # check if form is valid
        if form.is_valid():
            print("form is valid")
            form.save()
            # redirect
            return redirect("/leads")


    context = {
        "form" : form
    }
    return render(request, "leads/lead_create.html", context)


# updating the lead
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead" : lead
    }

    return render(request, "leads/lead_update.html", context)




# for reference
# creating a lead from 
# def lead_create(request):
#     form = LeadForm()  # empty form instantiation
#     # print(request.POST)

#     # check if method is POST 
#     if request.method == "POST":
#         print("Receiving a post request")
#         form = LeadForm(request.POST)
#         # check if form is valid
#         if form.is_valid():
#             print("form is valid")
#             print(form.cleaned_data)   # clean data dispaly 
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()  # first row in table  -> similar to .get
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             print("Lead has been created")
#             # redirect
#             return redirect("/leads")


#     context = {
#         "form" : form
#     }
#     return render(request, "leads/lead_create.html", context)