from django.urls import path
from .views import  (
    lead_list, lead_detail, lead_create, lead_update, lead_delete, 
    LeadListView
)

app_name = "leads"

# create a urlpattern list
urlpatterns =[
    # path('', lead_list, name='lead-list'), 
    path('', LeadListView.as_view(), name='lead-list'),
    # path('create/', lead_create),
    # use pk to uniquely identify a lead
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create/', lead_create, name='lead-create'),
]