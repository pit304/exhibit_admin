from django.contrib import admin

from .models import Atelier, Project, Publication, Competition, Image, Plan

admin.site.site_header = 'Exhibit administration'
admin.site.site_title = 'Exhibit site admin'
admin.site.index_title = 'Site administration'

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class PlanInline(admin.TabularInline):
    model = Plan
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['project_title', 'project_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ImageInline, PlanInline]
    list_display = ('project_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['project_title']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Atelier)
admin.site.register(Publication)
admin.site.register(Competition)