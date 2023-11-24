from django.contrib import admin

from .models import Project


# Register your models here.


# esta clase sirve para mostrar la fecha de creacion y la de actualizacion
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Project, ProjectAdmin)
