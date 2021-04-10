from django.shortcuts import render
from django.http import HttpResponse
# import the leads model
from .models import Lead


# function based views

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
    print(pk)
    # use pk to retrieve specific row using object manager
    lead = Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse("Here is the leads view")

    