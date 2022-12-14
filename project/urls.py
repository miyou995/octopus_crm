from django.urls import path 
   
from project.views import ProjectListView, AddProjectView, ProjectUpdateView, ProjectDetailView,ProjectDeleteView
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView
from .views import TeamListView, TeamCreateView, TeamUpdateView, TeamDeleteView, TeamDetailView
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'project'

urlpatterns = [
  
   #project
   path('projectlist', login_required(ProjectListView.as_view()), name='projectlist'),
   path('addproject', login_required(AddProjectView.as_view()), name="addproject"),
   path('editproject/<int:pk>/', login_required(ProjectUpdateView.as_view()), name="editproject"),
   path('projectdetail/<int:pk>/', login_required(ProjectDetailView.as_view()), name="projectdetail"),
   path('projectdelete/<int:pk>/', login_required(ProjectDeleteView.as_view()), name="projectdelete"),

   #Tasks
   path('tasklist', login_required(TaskListView.as_view()), name='tasklist'),
   path('addtask', login_required(TaskCreateView.as_view()), name="addtask"),
   path('edittask/<int:pk>/', login_required(TaskUpdateView.as_view()), name="edittask"),
   path('taskdetail/<int:pk>/', login_required(TaskDetailView.as_view()), name="taskdetail"),
   path('taskdelete/<int:pk>/', login_required(TaskDeleteView.as_view()), name="taskdelete"),

   #teams
   path('teams', login_required(TeamListView.as_view()), name="teamlist"),
   path('addteam', login_required(TeamCreateView.as_view()), name="addteam"),
   path('editteam/<int:pk>/', login_required(TeamUpdateView.as_view()), name="editteam"),
   path('teamdelete/<int:pk>/', login_required(TeamDeleteView.as_view()), name="teamdelete"),
   path('teamdetail/<int:pk>/', login_required(TeamDetailView.as_view()), name="teamdetail"),



]




