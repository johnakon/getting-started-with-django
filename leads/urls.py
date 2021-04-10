from django.urls import path
from .views import  lead_list

app_name = "leads"

# create a urlpattern list
urlpatterns =[
    path('', lead_list)
]