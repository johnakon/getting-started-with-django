from django.shortcuts import render
from django.http import HttpResponse
# import the leads model
from .models import Lead


# function based views
def lead_list(request):

    # fetch all leads and store in a variable leads
    leads = Lead.objects.all()

    context={
        "leads" : leads
    }
    return render(request, "leads/lead_list.html", context)