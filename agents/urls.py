from django.urls import path
from .views import AgentList,Agentcreate,AgentDetail,AgentUpdate

app_name='agents'

urlpatterns=[
    path('',AgentList.as_view(),name='agents-list'),
    path('create',Agentcreate.as_view(),name='agent-create'),
    path('<int:pk>/',AgentDetail.as_view(),name='agent-detail'),
    path('<int:pk>/update',AgentUpdate.as_view(),name='agent-update')

]
