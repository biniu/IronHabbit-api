from django.contrib import admin
from .models import Task, Project, Habbit, Dailies, DailiesDoneList

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Habbit)
admin.site.register(Dailies)
admin.site.register(DailiesDoneList)
