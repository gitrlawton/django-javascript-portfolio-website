from django.contrib import admin

## Register your models here (so we can see them from the admin panel.) ##
from .models import Tag, Project, ProjectImage

## Custom Registration. ##
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1   # How many of these we are going to be displaying inline (one image.)
    

class ProjectAdmin(admin.ModelAdmin):
    # When we're viewing a list of all the different projects, it's going to
    # show the title and a link.
    list_display = (
        "title",
        "link"
    )
    inline = [ProjectImageInline]
    search_fields = (
        "title",
        "description"
    )
    # Trailing comma is needed in order for this to be accepted as a tuple,
    # since there is only one element.
    list_filter = ("tags",)
    
class TagAdmin(admin.ModelAdmin):
    # Trailing comma is needed in order for this to be accepted as a tuple,
    # since there is only one element.
    list_display = ("name",)
    search_fields = ("name",)
    
# Registering the models with their customizations.
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
