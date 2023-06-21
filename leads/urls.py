from django.urls import path
from .views import leads_list,lead_detail,lead_update,lead_delete,LeadCreate

app_name='leads'

urlpatterns=[
      path('',leads_list,name='leads-list'),
      path('<int:pk>/',lead_detail,name='lead-detail'),
      path('<int:pk>/update/',lead_update,name='lead-update'),
      path('<int:pk>/delete/',lead_delete,name='lead-delete'),
      path('create',LeadCreate.as_view(),name='lead-create'),
]