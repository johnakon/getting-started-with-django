from django.urls import path
from .views import  lead_list, lead_detail

app_name = "leads"

# create a urlpattern list
urlpatterns =[
    path('', lead_list),
    # use pk to uniquely identify a lead
    path('<pk>/', lead_detail)
]