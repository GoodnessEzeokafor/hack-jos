from  django.urls import include, path
from . import views

urlpatterns = [  
	path('teams/', views.TeamList.as_view(), name='team-list'),
	path('<int:pk>/team/', views.TeamDetail.as_view(), name='team-detail'),
    path('participants/', views.ParticipantList.as_view(), name='participant-list'),
    path('<int:pk>/participants/', views.ParticipantsDetails.as_view(), name='participants-details')
]

