from django.contrib import admin

from .models import Atelier, Project, Publication, Competition, Image

admin.site.site_header = 'Exhibit administration'
admin.site.site_title = 'Exhibit site admin'
admin.site.index_title = 'Site administration'

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    fields = ['image_tag', 'title', 'image', 'is_plan', 'order', 'active']
    readonly_fields = ['image_tag']

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('project_title', 'order', 'active')
    search_fields = ['project_title']

class AtelierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['atelier_text']})
    ]
    list_display = ['abstract']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Atelier, AtelierAdmin)
admin.site.register(Publication)
admin.site.register(Competition)