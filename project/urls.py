from django.urls import path 
   
from project.views import ProjectListView, AddProjectView, ProjectUpdateView, ProjectDetailView,ProjectDeleteView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'project'

urlpatterns = [
  
   #project
   path('projectlist', login_required(ProjectListView.as_view()), name='projectlist'),
   path('addproject', login_required(AddProjectView.as_view()), name="addproject"),
   path('editproject/<int:pk>/', login_required(ProjectUpdateView.as_view()), name="editproject"),
   path('projectdetail/<int:pk>/', login_required(ProjectDetailView.as_view()), name="projectdetail"),
   path('projectdelete/<int:pk>/', login_required(ProjectDeleteView.as_view()), name="projectdelete"),

   
   

]




