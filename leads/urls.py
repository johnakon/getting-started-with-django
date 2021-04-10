from django.urls import path
from .views import  lead_list, lead_detail, lead_create

app_name = "leads"

# create a urlpattern list
urlpatterns =[
    path('', lead_list),
    # path('create/', lead_create),
    # use pk to uniquely identify a lead
    path('<int:pk>/', lead_detail),
    path('create/', lead_create)
]