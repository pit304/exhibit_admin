from django.contrib import admin

from .models import Atelier, Project, Publication, Competition

admin.site.register(Atelier)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Competition)