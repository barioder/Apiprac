
from django.urls import path
from .views import (list_pp_agents, pp_Agent, pp_agentapi_view, api_view_pp_Agent, 
ClassViewPpAgent, ClassViewAgentDetails, GenericApiView)

urlpatterns = [
    path('agents/', list_pp_agents),
    path('pp_agent/<int:id>/', pp_Agent),
    path('api_view', pp_agentapi_view),
    path('api_view/<int:id>/', api_view_pp_Agent),
    path('classapi/', ClassViewPpAgent.as_view()),
    path('classapi/<int:id>/', ClassViewAgentDetails.as_view()),
    path('genericapi/<int:id>/', GenericApiView.as_view()),

]
