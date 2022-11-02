from django.contrib import admin
from project.models import Project, Teams
# from import_export.admin import ImportExportModelAdmin  



# @admin.register(Project)
# class ProjectImportExport(ImportExportModelAdmin) : 
#     pass  


admin.site.register(Teams)
admin.site.register(Project)