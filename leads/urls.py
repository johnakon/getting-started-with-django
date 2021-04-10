from django.urls import path
from .views import  lead_list, lead_detail, lead_create, lead_update

app_name = "leads"

# create a urlpattern list
urlpatterns =[
    path('', lead_list),
    # path('create/', lead_create),
    # use pk to uniquely identify a lead
    path('<int:pk>/', lead_detail),
    path('<int:pk>/update/', lead_update),
    path('create/', lead_create),
]